import numpy as np

from example_functions import target_function_dict
from line_search_methods import line_search_dict
from main_methods import main_method_dict
from config import best_params
from helpers import generate_x0


def run_one(_theta, _main_method, _ls_method, params, ls_params):
    theta = _theta()
    x0 = generate_x0(theta.n, *theta.bounds)
    ls_method = _ls_method(ls_params)
    main_method = _main_method(params, ls_method)

    # print('Correct solution: ', theta.min_values)
    result = main_method(theta, np.array(x0))
    # print('Found solution: ', result['min_value'])
    # print(result_to_string(result))
    return result


def result_to_string(result):
    perf = result['performance']
    ls_perf = perf['line_search']
    return ', '.join([str(s) for s in [
        result['status'], perf['iterations'], f"{perf['duration']} ms",
        ls_perf['iterations'], f"{round(ls_perf['duration'], 2)} ms",
    ]])


np.warnings.filterwarnings('ignore', category=RuntimeWarning)

for theta in best_params:
    for main_method in best_params[theta]:
        for line_search in best_params[theta][main_method]:
            result = run_one(
                target_function_dict[theta],
                main_method_dict[main_method],
                line_search_dict[line_search],
                best_params[theta][main_method][line_search]['params'],
                best_params[theta][main_method][line_search]['ls_params'],
            )
            status = result['status']
            print(f"{status}: {theta},{main_method},{line_search}")
