import json

import numpy as np

from example_functions import visualization_function_dict
from line_search_methods import line_search_dict
from main_methods import main_method_dict
from config import visualization_params as v_params
from helpers import generate_x0


def run_one(_theta, _main_method, _ls_method, params, ls_params, x0=None):
    theta = _theta()
    if x0 is None:
        x0 = generate_x0(theta.n, *theta.bounds)
    ls_method = _ls_method(ls_params)
    main_method = _main_method(params, ls_method)

    result = main_method(theta, np.array(x0))
    return result


def result_to_string(result):
    perf = result['performance']
    ls_perf = perf['line_search']
    return ', '.join([str(s) for s in [
        result['status'], perf['iterations'], f"{perf['duration']} ms",
        ls_perf['iterations'], f"{round(ls_perf['duration'], 2)} ms",
    ]])


np.warnings.filterwarnings('ignore', category=RuntimeWarning)


# for i, theta in enumerate(visualization_function_dict):
# output = {}
theta = 'Himmelblau'
# for j, main_method in enumerate(v_params):
main_method = 'NewtonsMethod'
output = {theta: {main_method: {}}}
for k, line_search in enumerate(v_params[main_method]):
    print(
        f'\nNow running: {theta} + {main_method} + ' +
        f'{line_search}'
    )
    print(
        # f'Total progress - theta: {i + 1}/' +
        f'{len(visualization_function_dict)}, ' +
        # f'main method: {j + 1}/{len(v_params)}, ' +
        f'line search: {k + 1}/{len(v_params[main_method])}, '
    )
    # line_search = 'ConstantSearch'
    result = run_one(
        visualization_function_dict[theta],
        main_method_dict[main_method],
        line_search_dict[line_search],
        v_params[main_method][line_search]['params'],
        v_params[main_method][line_search]['ls_params'],
        x0=[[0.0], [0.0]]
    )
    status = result['status']
    if not status:
        print(f">>> FAILURE {theta},{main_method},{line_search}")
    steps = [
        p.reshape(1, 2).flatten().tolist() for p in result['steps']
    ]
    print(steps[0])
    # print(steps)
    # output[theta] = {main_method: {line_search: steps}}
    output[theta][main_method][line_search] = steps

with open('visualization/steps.js', 'w') as f:
    f.write(f'const stepData = {json.dumps(output)}')
