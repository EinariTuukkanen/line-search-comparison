import time
# import random
# import itertools
import multiprocessing

import progressbar
import numpy as np

from example_functions import target_function_dict
from line_search_methods import line_search_dict
from main_methods import main_method_dict
from config import best_params
from helpers import Result, generate_x0_dist
# from export import export_final_params_latex
from export import export_raw_performances_csv

np.warnings.filterwarnings('ignore', category=RuntimeWarning)


class Worker(multiprocessing.Process):

    def __init__(self, task_queue, result_queue):
        multiprocessing.Process.__init__(self)
        self.task_queue = task_queue
        self.result_queue = result_queue

    def run(self):
        while True:
            next_task = self.task_queue.get()
            if next_task is None:
                # Poison pill means shutdown
                # print('{}: Exiting'.format(proc_name))
                self.task_queue.task_done()
                break
            result = next_task()
            self.result_queue.put(result)
            self.task_queue.task_done()


class BarWorker(multiprocessing.Process):
    def __init__(self, bar, task_queue, task_count):
        multiprocessing.Process.__init__(self)
        self.bar = bar
        self.task_queue = task_queue
        self.task_count = task_count

    def run(self):
        while True:
            s = self.task_queue.qsize()
            self.bar.update(self.task_count - min(s, self.task_count))
            if s == 0:
                break


class Task:

    def __init__(self, args):
        self.args = args

    def __call__(self):
        theta_cls = target_function_dict[self.args['theta_name']]
        line_search_cls = line_search_dict[self.args['line_search_name']]
        main_method_cls = main_method_dict[self.args['main_method_name']]

        theta = theta_cls(rnd_seed=self.args['theta_rnd_seed'])
        line_search = line_search_cls(self.args['ls_params'])
        main_method = main_method_cls(self.args['params'], line_search)

        x0 = np.array(self.args['x0'])
        if x0.shape != (len(x0), 1):
            x0 = x0.reshape(len(x0), 1)

        result = main_method(theta, x0)
        result['args'] = self.args
        return result

    def __str__(self):
        return (
            f'{self.theta_name}, {self.main_method_name}, ' +
            f'{self.line_search_name}'
        )


if __name__ == '__main__':
    start_time = time.time()
    # Create multiprocessing containers and workers
    tasks = multiprocessing.JoinableQueue()
    results = multiprocessing.Queue()

    point_count = 1000  # Point count to test for
    num_workers = multiprocessing.cpu_count() * 2
    print(f'Creating {num_workers} workers')
    workers = [Worker(tasks, results) for i in range(num_workers)]
    for w in workers:
        w.start()
    task_count = 0

    # Loop over target functions
    for i, (theta_name, _main_methods) in enumerate(best_params.items()):
        # Increase randomness by creating unique thetas for each x0
        theta_rnd_seeds = [i for i in range(point_count)]
        theta_cls = target_function_dict.get(theta_name)

        try:
            x0s = np.loadtxt(f'data/x0s_{point_count}_{theta_name}.txt')
            x0s = np.hsplit(x0s, point_count)
            print('Succesfully loaded existing data.')
        except Exception as e:
            min_dist = theta_cls().min_dists.get(point_count, 0)
            print('Could not find existing data: ', e)
            print('Generating new data with min dist ', min_dist)
            # TODO: Move these variables to the class, not instance
            x0s = generate_x0_dist(
                point_count,
                min_dist,
                theta_cls().n,
                *theta_cls().bounds
            )
            np.savetxt(
                f'data/x0s_{point_count}_{theta_name}.txt',
                np.column_stack(x0s)
            )

        # Loop over main methods
        for j, (main_method_name, _ls_methods) in \
                enumerate(_main_methods.items()):

            # Loop over line search methods
            for k, (line_search_name, test) in enumerate(_ls_methods.items()):
                # Create the permutations of parameters
                task_count += len(x0s)
                param_keys = [*test['params'].keys()]
                ls_param_keys = [*test['ls_params'].keys()]
                p = (*test['params'], *test['ls_params'])

                # Format the params
                params = {key: p[i] for i, key in enumerate(param_keys)}
                ls_params = {
                    key: p[i + len(param_keys)]
                    for i, key in enumerate(ls_param_keys)
                }

                # Test for each starting point and function
                for i, x0 in enumerate(x0s):
                    args = {
                        'x0': x0.tolist(),
                        'theta_name': theta_name,
                        'main_method_name': main_method_name,
                        'line_search_name': line_search_name,
                        'params': test['params'],
                        'ls_params': test['ls_params'],
                        'permutation': p,
                        'test_params': test['params'],
                        'test_ls_params': test['ls_params'],
                        'theta_rnd_seed': theta_rnd_seeds[i],
                    }
                    tasks.put(Task(args))

    print(f'Task count: {task_count}.')

    bar = progressbar.ProgressBar(
        maxval=task_count,
        widgets=[
            progressbar.Percentage(), ' (',
            progressbar.Counter(), f'/{task_count}) ',
            progressbar.Bar('=', '[', ']'), ' ',
            progressbar.ETA(), ' ',
            progressbar.AdaptiveETA(),
        ]
    )
    bar.start()
    bar_worker = BarWorker(bar, tasks, task_count)
    bar_worker.start()

    for i in range(num_workers):
        tasks.put(None)
    tasks.join()

    result_dict = {}
    while task_count:
        r = Result(results.get())
        permutations = (
            result_dict
            .get(r.args['theta_name'], {})
            .get(r.args['main_method_name'], {})
            .get(r.args['line_search_name'], [])
        )
        existing = next((p for p in permutations if p.is_same(r)), None)
        if existing:
            existing += r
        else:
            (result_dict
                .setdefault(r.args['theta_name'], {})
                .setdefault(r.args['main_method_name'], {})
                .setdefault(r.args['line_search_name'], [])).append(r)
        task_count -= 1

    print('\n')
    for th in result_dict.values():
        for mm in th.values():
            for ls in mm.values():
                print(f'==> BEST: {min(ls).performance_str()}')
                # print(ls[0].get_raw_performances())

    print(f'\nProgram completed in {time.time() - start_time} seconds.')

    # export_final_params_latex(result_dict, 'NegativeEntropy', point_count)
    # export_final_params_latex(result_dict, 'MatrixSquareSum', point_count)
    result = result_dict['MatrixSquareSum']['NewtonsMethod']['DichotomousSearch'][0]
    m = result.m()
    perf = result.performance
    row = ' & '.join(map(lambda x: str(x), [
        'DichotomousSearch',
        round(result.success_rate(), 1),
        round(perf['main_method']['duration'] / m, 1),
        round(perf['main_method']['iterations'] / m, 1),
        round(perf['theta']['function_calls'] / m, 1),
        round(perf['line_search']['duration'] / m, 1),
        round(perf['line_search']['iterations'] / m, 1),
    ]))
    print(row)
    export_raw_performances_csv(result_dict)
