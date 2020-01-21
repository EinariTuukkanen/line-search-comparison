import random
import time
import copy

import numpy as np

from line_search_methods import line_search_dict
from main_methods import main_method_dict


class Result:
    comparables = [
        'theta_name',
        'main_method_name',
        'line_search_name',
        'permutation'
    ]

    def __init__(self, result):
        self.result = result
        self.args = result['args']
        self.successful = int(result['status'])
        self.x0s = [self.args['x0']]
        self.performance = result['performance']
        self.m = lambda: len(self.x0s)
        self.success_rate = lambda: self.successful / self.m() * 100
        self.performances = [copy.deepcopy(result['performance'])]
        self.statuses = [int(result['status'])]

    def __add__(self, other):
        result = other.result
        self.successful += result['status']
        self.x0s.append(other.args['x0'])
        performance = result['performance']
        for header in performance:
            for key, value in performance[header].items():
                self.performance[header][key] += value
        self.performances.append(performance)
        self.statuses.append(result['status'])
        return self

    def __str__(self):
        perf = self.performance
        opt_params, opt_ls_params = self.get_optimized_params()
        return (
            ', '.join([str(self.args[k]) for k in self.comparables[:-1]]) +
            f' {str(opt_params)}, {str(opt_ls_params)}, ' +
            f'\t\t{self.success_rate()}%, ' +
            ', '.join([
                str(round(perf['main_method']['iterations'] / self.m())),
                f"{round(perf['main_method']['duration'] / self.m(), 1)}ms",
                str(round(perf['line_search']['iterations'] / self.m())),
                f"{round(perf['line_search']['duration'] / self.m(), 1)}ms",
                f"{round(perf['theta']['function_calls'] / self.m(), 1)}fn",
                f"{round(perf['theta']['domain_iterations'] / self.m(), 1)}di",
            ])
        )

    def __gt__(self, other):
        """ Self worse than other """
        # First priority is success rate
        if self.successful < other.successful:
            return True

        if self.successful > other.successful:
            return False

        # Second priority is total duration of the method
        d1 = self.performance['main_method']['duration']
        d2 = other.performance['main_method']['duration']
        return d1 > d2

    def __eq__(self, other):
        d1 = self.performance['main_method']['duration']
        d2 = other.performance['main_method']['duration']
        return (
            self.successful == other.successful and
            d1 == d2
        )

    def __ge__(self, other):
        return self == other or self > other

    def is_same(self, other):
        """ Is same permutation (i.e. different starting point) """
        for k in self.comparables:
            if self.args[k] != other.args[k]:
                return False
        return True

    def get_optimized_params(self):
        optimized = {}
        for param, value in self.args['params'].items():
            if len(self.args['test_params'][param]) > 1:
                optimized[param] = value

        optimized_ls = {}
        for param, value in self.args['ls_params'].items():
            if len(self.args['test_ls_params'][param]) > 1:
                optimized_ls[param] = value

        return optimized, optimized_ls

    def performance_str(self):
        perf = self.performance
        return (
            ', '.join([str(self.args[k]) for k in self.comparables[:-1]]) +
            f'\t\t{self.success_rate()}%, ' +
            ', '.join([
                str(round(perf['main_method']['iterations'] / self.m())),
                f"{round(perf['main_method']['duration'] / self.m(), 1)}ms",
                str(round(perf['line_search']['iterations'] / self.m())),
                f"{round(perf['line_search']['duration'] / self.m(), 1)}ms",
                f"{round(perf['theta']['function_calls'] / self.m(), 1)}fn",
                f"{round(perf['theta']['domain_iterations'] / self.m(), 1)}di",
            ])
        )

    def get_raw_performances(self):
        return [
            (self.statuses[i],
             p['main_method']['iterations'],
             p['main_method']['duration'],
             p['line_search']['iterations'],
             p['line_search']['duration'],
             p['theta']['function_calls'],
             p['theta']['domain_iterations'])
            for i, p in enumerate(self.performances)
        ]


class Configuration:

    def __init__(
            self, theta, points, test_params, test_ls_params, main_method,
            line_search, params, ls_params):
        self.theta = theta
        self.points = points
        self.point_count = len(self.points)

        self.main_method = main_method
        self.test_params = test_params
        self.params = params

        self.line_search = line_search
        self.test_ls_params = test_ls_params
        self.ls_params = ls_params

        self.successful = 0
        self.performance = {
            'main_method': {
                'iterations': 0,
                'duration': 0,
            },
            'line_search': {
                'iterations': 0,
                'duration': 0,
            },
            'theta': {
                'domain_iterations': 0,
                'function_calls': 0,
            },
        }

    def per_run(self, header, key):
        return round(self.performance[header][key] / self.point_count, 1)

    def total_iterations(self):
        return self.performance['main_method']['iterations'] + \
            self.performance['line_search']['iterations']

    def update(self, result):
        self.successful += result.get('status')
        performance = result.get('performance')
        for header in performance:
            for key, value in performance[header].items():
                self.performance[header][key] += value

    def __gt__(self, other):
        """ Self worse than other """

        # First priority is success rate
        if self.successful < other.successful:
            return True

        # Second priority is total iterations (sum of main and line search)
        return self.total_iterations() > other.total_iterations()

    def __eq__(self, other):
        return (
            self.successful == other.successful and
            self.total_iterations() == other.total_iterations()
        )

    def __ge__(self, other):
        return self == other or self > other

    def __str__(self):
        return ', '.join([
            self.theta.__name__, self.main_method.__name__,
            self.line_search.__name__,
            f'{round(self.successful * 100 / self.point_count, 1)} %',
            f"{self.per_run('main_method', 'iterations')} iters",
            f"{self.per_run('main_method', 'duration')} ms",
            f"{self.per_run('line_search', 'iterations')} iters",
            f"{self.per_run('line_search', 'duration')} ms",
            f"{self.per_run('theta', 'function_calls')} fn",
            f"{self.per_run('theta', 'domain_iterations')} domain iters",
            str(self.params), str(self.ls_params),
        ])

    def get_optimized_params(self):
        optimized = {}
        for param, value in self.params.items():
            if len(self.test_params.get(param)) > 1:
                optimized[param] = value

        optimized_ls = {}
        for param, value in self.ls_params.items():
            if len(self.test_ls_params.get(param)) > 1:
                optimized_ls[param] = value

        return optimized, optimized_ls


def generate_x0(n, x_min, x_max):
    return np.array([
        random.random() * (abs(x_min) + abs(x_max)) - abs(x_min)
        for i in range(n)
    ]).reshape(n, 1)


def generate_x0_dist(count, min_dist, n, x_min, x_max):
    """ Generates more evenly distributed x0's """
    t1 = time.time()
    x0s = []
    i = 0
    k, max_iters = 0, 100000  # Safety feature
    while i < count and k < max_iters:
        k += 1
        is_good = True
        x = generate_x0(n, x_min, x_max)
        for p in x0s:
            if np.linalg.norm(p - x) < min_dist:
                is_good = False
                break
        if is_good:
            i += 1
            x0s.append(x)
    if k >= max_iters:
        raise Exception('Failed to find x0, too large min_dist?', min_dist)
    # Print little information message
    if count > 1:
        dists = []
        for i in range(count):
            for j in range(i + 1, count):
                dists.append(round(np.linalg.norm(x0s[i] - x0s[j]), 1))
        print(
            f'Generated {len(x0s)} points in {round(time.time() - t1, 1)}s ' +
            f'with (min, max) distance of ({min(dists)}, {max(dists)})'
        )
    return x0s


def get_averages(results):
    def avg(f):
        return round(sum([f(r) for r in results]) / len(results))
    return (
        f"""Average - success: {
            avg(lambda r: round(r.successful * 100 / r.n, 1))} %, """ +
        f"iters: {avg(lambda r: r.per_run('main_method', 'iterations'))}, " +
        f"""duration: {
            avg(lambda r: r.per_run('main_method', 'duration'))} ms, """ +
        f"""ls_iters: {
            avg(lambda r: r.per_run('line_search', 'iterations'))}, """ +
        f"""ls_duration: {
            avg(lambda r: r.per_run('line_search', 'iterations'))} ms, """ +
        f"fn: {avg(lambda r: r.per_run('theta', 'function_calls'))}, " +
        f"""domain_iters: {
            avg(lambda r: r.per_run('theta', 'domain_iterations'))}"""
    )


def generate_permutation_table(result_dict, theta_name, line_search_name):
    ls_cls = line_search_dict[line_search_name]

    header = [theta_name]
    subheader = []
    mm_symbols = []
    data = {}
    data_rows = {}
    for mm, line_searches in result_dict[theta_name].items():
        mm_cls = main_method_dict[mm]
        header.append('\\multicolumn{2}{c|}{' + f'{mm_cls.abbr}' + '}')
        mm_symbols += [*mm_cls.param_symbols.values()]
        data[mm_cls.abbr] = {}
        for r in line_searches[line_search_name]:
            data[mm_cls.abbr][r.args['permutation']] = tuple((
                r.success_rate(),
                r.performance['main_method']['duration']
            ))

            p1, p2 = r.get_optimized_params()
            p = str(tuple({**p1, **p2}.values()))

            if not data_rows.get(p):
                data_rows[p] = {}

            data_rows[p][mm_cls.abbr] = tuple((
                r.success_rate(),
                r.performance['main_method']['duration']
            ))

    # Generate subheader row
    subheader.append(
        f"$({','.join([*ls_cls.param_symbols.values(), *mm_symbols])})$"
    )
    subheader += ['$s$ (\\%)', '$t$ (ms)'] * (len(header) - 1)

    print(header)
    print(subheader)
    # print(json.dumps(data_rows, indent=2))

    # with open('output.tex', 'w') as f:
    #     f.write(' & '.join(header))
    #     f.write('\n')
    #     f.write(' & '.join(subheader))
    #     f.write('\n')
    #     for row in data_rows.values():
    #         f.write(' & '.join(row))
    #         f.write('\n')

    # for main_method_name, line_searches in result_dict[theta_name].items():
    #     perm, results = line_searches[line_search_name].items()

    # return f'(0.01, -10, 10)\t& 15\t& 1200\t& 11120\t\\'

    # return """
    #     \rowcolors{2}{white}{blue!15}
    #     \captionof{table}{Your caption here}
    #     \begin{tabular}{ |p{3cm}|p{3cm}|p{3cm}|p{3cm}| }
    #     \hline
    #     \rowcolor{blue!50}
    #     \multicolumn{4}{|c|}{Golden Section Search} \\
    #     \hline
    #     \rowcolor{blue!40}
    #     ($l, a, b$)     & duration (ms) & iterations    & $\theta_n$    \\
    #     \hline
    #     (0.01, -10, 10) & 15            & 1200          & 11120         \\
    #     (0.01, -10, 10) & 15            & 1200          & 11120         \\
    #     (0.01, -10, 10) & 15            & 1200          & 11120         \\
    #     \hline
    #     \end{tabular}
    # """
