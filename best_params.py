import itertools

import progressbar
import numpy as np

from example_functions import target_function_dict
from line_search_methods import line_search_dict
from main_methods import main_method_dict
from config import test_params
from helpers import Configuration, generate_x0_dist, get_averages

np.warnings.filterwarnings('ignore', category=RuntimeWarning)


def run_with_params(
         x0s, thetas,
        _theta, _main_method, _ls_method,
        test_params, test_ls_params):

    # Create the permutations of parameters
    permutations = list(itertools.product(
        *[*test_params.values(), *test_ls_params.values()]
    ))
    param_keys = [*test_params.keys()]
    ls_param_keys = [*test_ls_params.keys()]

    total_iterations = len(permutations) * len(x0s)
    bar = progressbar.ProgressBar(
        maxval=total_iterations,
        widgets=[
            progressbar.Percentage(), ' (',
            progressbar.Counter(), f'/{total_iterations}) ',
            progressbar.Bar('=', '[', ']'), ' ',
            progressbar.ETA(), ' ',
            progressbar.AdaptiveETA(),
        ]
    )
    bar.start()
    k = 0

    results = []
    for p in permutations:
        # Format the params
        params = {key: p[i] for i, key in enumerate(param_keys)}
        ls_params = {
            key: p[i + len(param_keys)]
            for i, key in enumerate(ls_param_keys)
        }

        ls_method = _ls_method(ls_params)
        main_method = _main_method(params, ls_method)
        current_config = Configuration(
            _theta, x0s, test_params, test_ls_params,
            _main_method, _ls_method, params, ls_params
        )

        # Test for each starting point and function
        for i, x0 in enumerate(x0s):
            theta = thetas[i]
            result = main_method(theta, np.array(x0))
            current_config.update(result)
            k += 1
            bar.update(k)

        results.append(current_config)
    bar.finish()

    return results


def optimize_params():
    # Generate sample data: random starting points and functions
    # n = 50  # Dimensions
    point_count = 100  # Point count to test for

    # For 100 points in 50 dimensions & [-10, 10] area, min_dist 56 seems good
    # x0s = generate_x0_dist(point_count, 56, n, 0, 10)

    for i, (theta_name, _main_methods) in enumerate(test_params.items()):
        # Generate theta functions
        theta = target_function_dict.get(theta_name)
        thetas = [theta() for _ in range(point_count)]
        x0s = generate_x0_dist(point_count, 28, theta().n, *theta().bounds)

        for j, (main_method_name, _ls_methods) in \
                enumerate(_main_methods.items()):
            for k, (ls_method_name, test) in enumerate(_ls_methods.items()):
                print(
                    f'\nNow running: {theta_name} + {main_method_name} + ' +
                    f'{ls_method_name}'
                )
                print(
                    f'Total progress - theta: {i + 1}/{len(test_params)}, ' +
                    f'main method: {j + 1}/{len(_main_methods)}, ' +
                    f'line search: {k + 1}/{len(_ls_methods)}, '
                )

                results = run_with_params(
                    x0s, thetas,
                    theta,
                    main_method_dict.get(main_method_name),
                    line_search_dict.get(ls_method_name),
                    test['params'],
                    test['ls_params']
                )

                # Printing some stats and results
                # for r in results:
                #     print(r)
                print(get_averages(results))
                best = min(results)
                print(f'===> Best: {str(best)}')
                params, ls_params = best.get_optimized_params()
                print(f'===> main method: {params}, line search: {ls_params}')


optimize_params()
