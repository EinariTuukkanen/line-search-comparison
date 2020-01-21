from time import time
import numpy as np
from numpy.linalg import norm, inv


class MainMethod:
    abbr = ''
    param_symbols = {}

    def __init__(self, params, line_search_method):
        self.params = params
        self.line_search_method = line_search_method
        self.name = type(self).__name__

        for (key, value) in params.items():
            setattr(self, key, value)

    def __call__(self, theta, x0, *args, **kwargs):
        start_time = time()
        min_point, steps, ls_performance, iters = self.run(
            theta, x0, **self.params
        )
        min_value = theta(min_point)
        status = self._is_equal_with_accuracy(min_value, theta.min_values, 8)

        if status and hasattr(self, 'max_iterations'):
            if iters >= self.max_iterations:
                print(f'Warning: {self.name} reached max iters ({iters}).')

        return {
            'status': status,
            'steps': steps,
            'min_point': min_point,
            'min_value': min_value,
            'performance': {
                'main_method': {
                    'iterations': iters,
                    'duration': round((time() - start_time) * 1000, 1),
                },
                'line_search': ls_performance,
                'theta': theta.performance,
            }
        }

    def run(self, **kwargs):
        raise NotImplementedError('Method must be overriden in subclass')

    def _is_equal_with_accuracy(self, value, correct_values, accuracy):
        """ Is value in list of correct values, with 'accuracy' decimals """
        return (
            round(np.float64(value), accuracy) in
            [round(p, accuracy) for p in correct_values]
        )


class NewtonsMethod(MainMethod):
    abbr = 'NM'

    def run(self, theta, x0, tolerance, max_iterations, **kwargs):
        ls_performance = {'iterations': 0, 'duration': 0}
        steps = [np.copy(x0)]
        x = x0
        k = 0

        while norm(theta.gradient(x)) > tolerance and k < max_iterations:
            d = np.array(
                -inv(theta.hessian(x)) @ theta.gradient(x)
            ).reshape(theta.n, 1)
            argmin = theta.get_step_size_function(x, d)
            optima = self.line_search_method(argmin)
            x += optima['min_point'] * d

            ls_performance['iterations'] += optima['performance']['iterations']
            ls_performance['duration'] += optima['performance']['duration']
            steps.append(np.copy(x))
            k += 1

        return x, steps, ls_performance, k


class GradientDescentMethod(MainMethod):
    abbr = 'GDM'

    def run(self, theta, x0, tolerance, max_iterations, *args, **kwargs):
        ls_performance = {'iterations': 0, 'duration': 0}
        steps = [np.copy(x0)]
        x = x0
        k = 0

        while norm(theta.gradient(x)) > tolerance and k < max_iterations:
            d = np.array(-theta.gradient(x)).reshape(theta.n, 1)
            argmin = theta.get_step_size_function(x, d)
            optima = self.line_search_method(argmin)
            x += optima['min_point'] * d

            ls_performance['iterations'] += optima['performance']['iterations']
            ls_performance['duration'] += optima['performance']['duration']
            steps.append(np.copy(x))
            k += 1

        return x, steps, ls_performance, k


class ConjugateGradientMethod(MainMethod):
    abbr = 'CGM'

    def run(self, theta, x0, tolerance, max_iterations, *args, **kwargs):
        ls_performance = {'iterations': 0, 'duration': 0}
        steps = [np.copy(x0)]
        x = x0
        k = 0
        n = theta.n  # TODO: Is this correct?

        d = -theta.gradient(x)

        while norm(theta.gradient(x)) > tolerance and k < max_iterations:
            y = np.copy(x)
            for j in range(n):
                y_prev = np.copy(y)
                argmin = theta.get_step_size_function(y, d)
                optima = self.line_search_method(argmin)
                y += optima['min_point'] * d
                p = norm(theta.gradient(y)) ** 2
                q = norm(theta.gradient(y_prev)) ** 2
                if p == 0.0:
                    alpha = 0
                else:
                    alpha = (p / q)
                d = -theta.gradient(y) + alpha * d
                ls_performance['iterations'] += \
                    optima['performance']['iterations']
                ls_performance['duration'] += optima['performance']['duration']
                steps.append(np.copy(x))
                k += 1
            x = np.copy(y)
            d = theta.gradient(x)

        return x, steps, ls_performance, k


class HeavyBallMethod(MainMethod):
    abbr = 'HBM'
    param_symbols = {
        'beta': '\\beta_{HBM}'
    }

    def run(self, theta, x0, tolerance, beta, max_iterations, *args, **kwargs):
        ls_performance = {'iterations': 0, 'duration': 0}
        steps = [np.copy(x0)]
        x = x0
        x_prev = x0
        k = 0

        while norm(theta.gradient(x)) > tolerance and k < max_iterations:
            d = -theta.gradient(x) + beta * (x - x_prev)
            argmin = theta.get_step_size_function(x, d)
            optima = self.line_search_method(argmin)
            x_prev = np.copy(x)
            x += optima['min_point'] * d

            ls_performance['iterations'] += optima['performance']['iterations']
            ls_performance['duration'] += optima['performance']['duration']
            steps.append(np.copy(x))
            k += 1

        return x, steps, ls_performance, k


main_method_dict = {c.__name__: c for c in MainMethod.__subclasses__()}
