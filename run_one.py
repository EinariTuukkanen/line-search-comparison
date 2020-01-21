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

    print('Correct: ', theta.min_values)
    result = main_method(theta, np.array(x0))
    print('Guess: ', result['min_value'])
    print(result_to_string(result))


def result_to_string(result):
    perf = result['performance']
    mm_perf = perf['main_method']
    ls_perf = perf['line_search']
    return ', '.join([str(s) for s in [
        result['status'], mm_perf['iterations'], f"{mm_perf['duration']} ms",
        ls_perf['iterations'], f"{round(ls_perf['duration'], 2)} ms",
    ]])


theta = 'MatrixSquareSum'
main_method = 'ConjugateGradientMethod'
line_search = 'ConstantSearch'

run_one(
    target_function_dict.get(theta),
    main_method_dict.get(main_method),
    line_search_dict.get(line_search),
    best_params.get(theta).get(main_method).get(line_search).get('params'),
    best_params.get(theta).get(main_method).get(line_search).get('ls_params'),
)
