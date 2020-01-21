import autograd
import autograd.numpy as np
from autograd.numpy.linalg import norm, inv

from config import defaults


class TargetFunction:

    def __init__(self, n, bounds, min_dists, params={}, min_points=[]):
        self.n = n
        self.bounds = bounds
        self.min_dists = min_dists
        self.params = params
        self.gradient = autograd.grad(self.__call__)
        _hessian = autograd.hessian(self.__call__)
        self.hessian = lambda x: np.asmatrix(_hessian(x))

        self.performance = {
            'function_calls': 0,
            'domain_iterations': 0,
        }

        self.min_points = min_points
        self.min_values = [self(p) for p in self.min_points]

    def __call__(self, x, *args, **kwargs):
        self.performance['function_calls'] += 1
        return self.run(x, *args, **kwargs)

    def run(self, x, *args, **kwargs):
        raise NotImplementedError('Method must be overriden in subclass')

    def domain(self, x, l, d, gamma=None):
        return l

    def get_step_size_function(self, x, d):
        def f(l): return self.__call__(x + l * d)
        _derivative = autograd.grad(f)
        _derivative2 = autograd.grad(_derivative)
        f.derivative = lambda l: _derivative(np.float64(l))
        f.derivative2 = lambda l: _derivative2(np.float64(l))
        f.domain = lambda l, gamma: self.domain(x, l, d, gamma)
        return f


class NegativeEntropy(TargetFunction):

    def __init__(self, n=50, bounds=[0, 10], min_dist=32, params={}, **kwargs):
        min_dists = {
            10: 32,
            100: 28,
            1000: 24,
        }
        params = defaults
        min_points = [np.ones(n) / np.array([np.exp(1)] * n)]
        super().__init__(n, bounds, min_dists, params, min_points)

    def run(self, x, *args, **kwargs):
        return np.sum(x * np.log(x))

    def domain(self, x, l, d, gamma=None):
        if not gamma:
            gamma = self.params.get('gamma', 0)
        k, max_iterations = 0, self.params.get('max_domain_iterations')
        while np.min(x + l * d) <= 0 and k < max_iterations:
            l *= gamma  # noqa
            k += 1
        if k >= max_iterations:
            print('Domain warning - max iterations reached! Setting l = 0.')
            l = 0.0  # noqa
        self.performance['domain_iterations'] += k
        return l


class MatrixSquareSum(TargetFunction):

    def __init__(self, n=50, bounds=[-10, 10], rnd_seed=None,
                 A=None, b=None, c=None, params=defaults, **kwargs):
        min_dists = {
            10: 64,
            100: 56,
            1000: 48,
        }
        self.params = params
        self.rnd_seed = rnd_seed if rnd_seed else np.random.randint(0, 1e3)
        _A, _b, _c = self._generate_data(n)
        self.A = _A if A is None else A
        self.b = _b if b is None else b
        self.c = _c if c is None else c

        min_points = [np.asarray(
            -inv(self.A.T * self.A + self.c * np.identity(n)) *
            self.A.T @ self.b
        ).reshape(n, 1)]

        super().__init__(n, bounds, min_dists, params, min_points)

    def run(self, x, *args, **kwargs):
        return (
            norm(np.asarray(self.A) @ x + self.b) ** 2 + self.c * norm(x) ** 2
        )

    def _generate_data(self, n):
        def _is_pos_def(x):
            return np.all(np.linalg.eigvals(x) > 0)
        np.random.seed(self.rnd_seed)
        A = np.matrix(np.random.rand(n, n) - np.ones([n, n]) * 0.5)
        A = (A + A.T)/2
        w, _ = np.linalg.eig(A)
        # d = Diagonal offset; smaller value = more elliptic i.e. harder for GD
        d = self.params.get('d')
        if not _is_pos_def(A):
            lmin = min(w)
            A = A + (abs(lmin) + d) * np.identity(n)
        assert(_is_pos_def(A))
        w, _ = np.linalg.eig(A)
        # condition_number = max(w) / min(w)

        b = (np.random.rand(n) - np.ones(n) * 0.5).reshape(n, 1)
        c = np.random.rand() - 0.5

        return A, b, c


class Himmelblau(TargetFunction):

    def __init__(self, n=2, bounds=[-10, 10], params=defaults,
                 **kwargs):
        min_points = [
            [3.584428, -1.848126],
            [-2.805118, 3.131312],
            [-3.779310, -3.283186],
            [3.0, 2.0],
        ]
        super().__init__(n, bounds, {}, params, min_points)

    def run(self, x, *args, **kwargs):
        x1, x2 = x
        return (x1 ** 2 + x2 - 11) ** 2 + (x1 + x2 ** 2 - 7) ** 2


class MatayasFunction(TargetFunction):

    def __init__(self, n=2, bounds=[-10, 10], params={}, **kwargs):
        min_points = [[0.0, 0.0]]
        super().__init__(n, bounds, {}, params, min_points)

    def run(self, x, *args, **kwargs):
        x1, x2 = x
        return 0.26 * (x1 ** 2 + x2 ** 2) - 0.48 * x1 * x2


class ExponentFunction(TargetFunction):

    def __init__(self, n=2, bounds=[-10, 10], params={}, **kwargs):
        min_points = [[-0.669072, 0.0]]
        super().__init__(n, bounds, {}, params, min_points)

    def run(self, x, *args, **kwargs):
        x1, x2 = x
        return x1 * np.exp(-(x1 ** 2 + x2 ** 2)) + (x1 ** 2 + x2 ** 2) / 20


target_function_dict = {
    'NegativeEntropy': NegativeEntropy,
    'MatrixSquareSum': MatrixSquareSum,
}

visualization_function_dict = {
    'Himmelblau': Himmelblau,
    'MatayasFunction': MatayasFunction,
    'ExponentFunction': ExponentFunction,
}
