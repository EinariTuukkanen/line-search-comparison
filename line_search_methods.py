from time import time
import numpy as np


class LineSearch:

    def __init__(self, params):
        self.name = type(self).__name__
        self.params = params

        for (key, value) in params.items():
            setattr(self, key, value)

    def __call__(self, theta, *args, **kwargs):
        start_time = time()
        min_point, steps, iters = self.run(theta, **self.params)
        if hasattr(self, 'max_iterations'):
            if iters >= self.max_iterations:
                print(
                    f'Warning: {self.name} reached max iters ({iters}), ' +
                    f'lambda: {min_point}, tolerance: {self.tolerance}.'
                )
        return {
            'steps': steps,
            'min_point': np.float64(min_point),
            'min_value': theta(min_point),
            'performance': {
                'iterations': iters,
                'duration': round((time() - start_time) * 1000, 1),
            }
        }

    def run(self, **kwargs):
        raise NotImplementedError('Method must be overriden in subclass')


class ConstantSearch(LineSearch):
    param_symbols = {
        'delta': '\\lambda',
    }

    def run(self, theta, delta, gamma=None, **kwargs):
        delta = theta.domain(delta, gamma)
        return [delta], delta, 0


class GoldenSectionSearch(LineSearch):
    param_symbols = {
        'a': 'a',
        'b': 'b',
        'tolerance': 'l',
    }

    def run(self, theta, a, b, tolerance, max_iterations,
            gamma=None, **kwargs):
        a = theta.domain(a, gamma)
        b = theta.domain(b, gamma)
        steps = [[a, b]]
        k = 0

        alpha = 0.618
        delta = a + (1 - alpha) * (b - a)
        mu = a + alpha * (b - a)

        while b - a > tolerance and k < max_iterations:
            if theta(delta) > theta(mu):
                a = delta
                delta = mu
                mu = a + alpha * (b - a)
            else:
                b = mu
                mu = delta
                delta = a + (1 - alpha) * (b - a)
            steps.append([a, b])
            k += 1

        return (a + b) / 2, steps, k


class BisectionSearch(LineSearch):
    param_symbols = {
        'a': 'a',
        'b': 'b',
        'tolerance': 'l',
    }

    def run(self, theta, a, b, tolerance, max_iterations,
            gamma=None, **kwargs):
        a = theta.domain(a, gamma)
        b = theta.domain(b, gamma)
        steps = [[a, b]]
        k = 0

        while abs(b - a) > tolerance and k < max_iterations:
            delta = (b + a) / 2
            # delta = theta.domain(a, gamma)
            dtheta = theta.derivative(delta)
            if dtheta == 0:
                break
            elif dtheta > 0:
                b = delta
            else:
                a = delta
            steps.append([a, b])
            k += 1

        return (a + b) / 2, steps, k


class DichotomousSearch(LineSearch):
    param_symbols = {
        'a': 'a',
        'b': 'b',
        'tolerance': 'l',
        'epsilon': '\\epsilon',
    }

    def run(self, theta, a, b, tolerance, epsilon,
            max_iterations, gamma=None, **kwargs):
        a = theta.domain(a, gamma)
        b = theta.domain(b, gamma)
        steps = [[a, b]]
        k = 0

        while b - a > tolerance and k < max_iterations:
            delta = (b + a) / 2 - epsilon
            mu = (b + a) / 2 + epsilon

            delta = theta.domain(delta, gamma)
            mu = theta.domain(mu, gamma)

            if theta(delta) < theta(mu):
                b = mu
            else:
                a = delta
            steps.append([a, b])
            k += 1

        return (a + b) / 2, steps, k


class FibonacciSearch(LineSearch):
    param_symbols = {
        'a': 'a',
        'b': 'b',
        'tolerance': 'l',
        'epsilon': '\\epsilon',
    }

    def fib(self, n):
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b
        return a

    def run(self, theta, a, b, tolerance, epsilon,
            max_iterations, gamma=None, **kwargs):
        a = theta.domain(a, gamma)
        b = theta.domain(b, gamma)
        steps = [[a, b]]
        k = 0

        n = 1
        while (b - a) / self.fib(n) > tolerance:
            n += 1

        delta = a + self.fib(n - 2) / self.fib(n) * (b - a)
        mu = a + self.fib(n - 1) / self.fib(n) * (b - a)

        while k <= n - 1 and k < max_iterations:
            if theta(delta) > theta(mu):
                a = delta
                delta = mu
                mu = a + self.fib(n - k - 1) / self.fib(n - k) * (b - a)
            else:
                b = mu
                mu = delta
                delta = a + self.fib(n - k - 2) / self.fib(n - k) * (b - a)
            steps.append([a, b])
            k += 1

        delta = theta.domain(delta, gamma)
        _mu = mu + epsilon
        _mu = theta.domain(_mu, gamma)
        if theta(delta) > theta(_mu):
            a = delta
        else:
            b = _mu

        return (a + b) / 2, steps, k


class UniformSearch(LineSearch):
    param_symbols = {
        'a': 'a',
        'b': 'b',
        'tolerance': 'l',
        'interval_count': 'n',
        'interval_multiplier': 'm',
    }

    def run(self, theta, a, b, tolerance, interval_count, interval_multiplier,
            max_iterations, gamma=None, **kwargs):
        a = theta.domain(a, gamma)
        # b = theta.domain(b, gamma)
        steps = [a]
        k = 0

        interval_size = (b - a) / interval_count
        min_point = a
        min_value = theta(a)

        while interval_size > tolerance and k < max_iterations:
            for i in range(interval_count + 1):
                k += 1
                x = a + i * interval_size
                x = theta.domain(x, gamma)
                y = theta(x)

                if y < min_value:
                    min_point = x
                    min_value = y
                    steps.append(x)

            a = min_point - interval_size
            b = min_point + interval_size
            interval_count = int(interval_count * interval_multiplier)
            interval_size = (b - a) / interval_count
        return min_point, steps, k


class NewtonsSearch(LineSearch):
    param_symbols = {
        'delta': '\\lambda',
        'tolerance': 'l',
    }

    def run(self, theta, delta, tolerance, max_iterations,
            gamma=None, **kwargs):
        delta = theta.domain(delta, gamma)
        steps = [delta]
        k = 0
        while abs(theta.derivative(delta)) > tolerance and k < max_iterations:
            delta = delta - theta.derivative(delta) / theta.derivative2(delta)
            delta = theta.domain(delta, gamma)
            steps.append(delta)
            k += 1
        return delta, steps, k


class ArmijoSearch(LineSearch):
    param_symbols = {
        'delta': '\\lambda',
        'alpha': '\\alpha',
        'beta': '\\beta',
    }

    def run(self, theta, delta, alpha, beta, max_iterations,
            gamma=None, **kwargs):
        delta = theta.domain(delta, gamma)
        steps = [delta]
        k = 0

        theta0 = theta(0)
        Dtheta0 = theta.derivative(0)

        condition = theta0 + alpha * delta * Dtheta0

        while theta(delta) > condition and k < max_iterations:
            delta *= beta
            condition = theta0 + alpha * delta * Dtheta0
            steps.append(delta)
            k += 1

        return delta, steps, k


line_search_dict = {c.__name__: c for c in LineSearch.__subclasses__()}
