defaults = {
    'gamma': 0.99,  # Multiplier to reduce step size if domain is invalid
    'd': 5,  # Diagonal offset for generating PD matrix
    'p': 0,  # Multiplier for offsetting negative entropy from zero
    'max_domain_iterations': 300000,  # Per calculation, max amount of laps
}

simple_test_params = {
    'MatrixSquareSum': {
        'params': {
            'NewtonsMethod': {'tolerance': [1e-4], 'max_iterations': [10000]},  # noqa
            'GradientDescentMethod': {'tolerance': [1e-4], 'max_iterations': [10000]},  # noqa
            'ConjugateGradientMethod': {'tolerance': [1e-4], 'max_iterations': [10000]},  # noqa
            'HeavyBallMethod': {'tolerance': [1e-4], 'beta': [0.1, 0.5, 1.0, 5.0, 10.0], 'max_iterations': [10000]},  # noqa
        },
        'ls_params': {
            # 'ConstantSearch': {'delta': [0.0001, 0.1, 0.25, 0.5, 0.9]},  # noqa
            # 'GoldenSectionSearch': {'a': [-10, -5], 'b': [10, 5], 'tolerance': [1e-4, 1e-7], 'max_iterations': [10000]},  # noqa
            # 'BisectionSearch': {'a': [-10, -5], 'b': [10, 5], 'tolerance': [1e-4, 1e-7], 'max_iterations': [10000]},  # noqa
            # 'BisectionSearch': {'a': [-10, -5], 'b': [10, 5], 'tolerance': [1, 1e-4], 'max_iterations': [10000]},  # noqa
            # 'DichotomousSearch': {'a': [-10, -5], 'b': [10, 5], 'epsilon': [1e-7, 1e-8], 'tolerance': [1e-4, 1e-5], 'max_iterations': [10000]},  # noqa
            # 'DichotomousSearch': {'a': [-10, -5], 'b': [10, 5], 'epsilon': [1e-7, 1e-10], 'tolerance': [1e-5, 1e-9], 'max_iterations': [10000]},  # noqa
            # 'FibonacciSearch': {'a': [-10, -5], 'b': [10, 5], 'epsilon': [1e-8, 1e-10, 1e-12], 'tolerance': [1e-6, 1e-10], 'max_iterations': [10000]},  # noqa
            # 'UniformSearch': {'a': [-10, -5], 'b': [10, 5], 'interval_count': [5, 10, 100], 'interval_multiplier': [1, 1.5, 2], 'tolerance': [1e-6, 1e-8], 'max_iterations': [10000]},  # noqa
            # 'NewtonsSearch': {'delta': [0.5, 1, 5, 10], 'tolerance': [1e-7, 1e-8], 'max_iterations': [10000]},  # noqa
            # 'ArmijoSearch': {'delta': [0.9, 1, 1.1], 'alpha': [0.1, 0.25, 0.5], 'beta': [0.5, 0.75, 0.9], 'tolerance': [1e-7], 'max_iterations': [10000]},  # noqa
            # 'ArmijoSearch': {'delta': [1], 'alpha': [0.5], 'beta': [0.75], 'tolerance': [1e-7], 'max_iterations': [10000]},  # noqa
            # 'ArmijoSearch': {'delta': [1], 'alpha': [0.25], 'beta': [0.5], 'tolerance': [1e-7], 'max_iterations': [10000]},  # noqa
            # 'ArmijoSearch': {'delta': [1], 'alpha': [0.45, 0.5, 0.55], 'beta': [0.65, 0.7, 0.75], 'tolerance': [1e-7], 'max_iterations': [10000]},  # noqa
            # 'ArmijoSearch': {'delta': [0.9, 1, 1.1], 'alpha': [0.1, 0.25, 0.5], 'beta': [0.5, 0.75, 0.9], 'tolerance': [1e-7], 'max_iterations': [10000]},  # noqa
            # 'ArmijoSearch': {'delta': [1], 'alpha': [0.1], 'beta': [0.5], 'tolerance': [1e-7], 'max_iterations': [10000]},  # noqa
        }
    },
    # 'NegativeEntropy': {
        # 'params': {
            # 'NewtonsMethod': {'tolerance': [1e-4], 'max_iterations': [10000]},  # noqa
            # 'GradientDescentMethod': {'tolerance': [1e-4], 'max_iterations': [10000]},  # noqa
            # 'ConjugateGradientMethod': {'tolerance': [1e-4], 'max_iterations': [10000]},  # noqa
    #         'HeavyBallMethod': {'tolerance': [1e-4], 'beta': [0.1, 0.5, 1.0], 'max_iterations': [10000]},  # noqa
        # },
        # 'ls_params': {
    #         'ConstantSearch': {'delta': [0.1, 0.25, 0.5]},  # noqa
            # 'GoldenSectionSearch': {'a': [-10, -5], 'b': [10, 5], 'tolerance': [1e-4, 1e-7], 'max_iterations': [10000]},  # noqa
            # 'BisectionSearch': {'a': [-10, -5], 'b': [10, 5], 'tolerance': [1e-4, 1e-7], 'max_iterations': [10000]},  # noqa
            # 'DichotomousSearch': {'a': [-10, -5], 'b': [5, 10], 'epsilon': [1e-6, 1e-7], 'tolerance': [1e-4, 1e-5], 'max_iterations': [10000]},  # noqa
            # 'FibonacciSearch': {'a': [-10, -5], 'b': [10, 5], 'epsilon': [1e-8, 1e-10, 1e-12], 'tolerance': [1e-6, 1e-12], 'max_iterations': [10000]},  # noqa
            # 'UniformSearch': {'a': [0, -5], 'b': [5, 10], 'interval_count': [5, 10, 20], 'interval_multiplier': [1, 1.5, 2], 'tolerance': [1e-5, 1e-6], 'max_iterations': [10000]},  # noqa
            # 'UniformSearch': {'a': [-5], 'b': [5], 'interval_count': [2], 'interval_multiplier': [1], 'tolerance': [1e-8], 'max_iterations': [10000]},  # noqa
            # 'NewtonsSearch': {'delta': [0.1, 0.5, 1, 5], 'tolerance': [1e-7, 1e-8], 'max_iterations': [100, 1000]},  # noqa
            # 'ArmijoSearch': {'delta': [0.9, 1, 1.1], 'alpha': [0.1, 0.25, 0.5], 'beta': [0.5, 0.75, 0.9], 'tolerance': [1e-7], 'max_iterations': [10000]},  # noqa
        #     'ArmijoSearch': {'delta': [1], 'alpha': [0.2, 0.25, 0.5], 'beta': [0.5, 0.75, 0.8], 'tolerance': [1e-7], 'max_iterations': [10000]},  # noqa
        # }
    # }
}

test_params = {}
for f in simple_test_params:
    test_params[f] = {}
    for m, p in simple_test_params[f]['params'].items():
        test_params[f][m] = {}
        for l, q in simple_test_params[f]['ls_params'].items():
            test_params[f][m][l] = {'params': p, 'ls_params': q}

overrides = {
    'MatrixSquareSum': {
        'NewtonsMethod': {
            'ConstantSearch': {
                'params': {'tolerance': [1e-4], 'max_iterations': [10000]},  # noqa
                'ls_params': {'delta': [0.5, 0.9, 1.0, 1.1, 1.5]},  # noqa
            },
            'DichotomousSearch': {
                'params': {'tolerance': [1e-4], 'max_iterations': [10000]},  # noqa
                'ls_params': {'a': [-10, -5], 'b': [10, 5], 'epsilon': [1e-7, 1e-10], 'tolerance': [1e-5, 1e-9], 'max_iterations': [10000]},  # noqa
            },
        }
    },
    'NegativeEntropy': {
        'NewtonsMethod': {
            'ConstantSearch': {
                'params': {'tolerance': [1e-4], 'max_iterations': [10000]},  # noqa
                'ls_params': {'delta': [0.1, 0.25, 0.5, 0.9]},  # noqa
            },
            'DichotomousSearch': {
                'params': {'tolerance': [1e-4], 'max_iterations': [10000]},  # noqa
                'ls_params': {'a': [-10], 'b': [5, 10], 'epsilon': [1e-6, 1e-7], 'tolerance': [1e-4, 1e-5], 'max_iterations': [10000]},  # noqa
            }
        },
        'ConjugateGradientMethod': {
            'ConstantSearch': {
                'params': {'tolerance': [1e-4], 'max_iterations': [10000]},  # noqa
                'ls_params': {'delta': [0.0001, 0.1, 0.15, 0.2]},  # noqa
            }
        }
    }
}

for i in overrides:
    for j in overrides[i]:
        for k, p in overrides[i][j].items():
            if (i in test_params and
                    j in test_params[i] and
                    k in test_params[i][j]):
                test_params[i][j][k]['params'] = p['params']
                test_params[i][j][k]['ls_params'] = p['ls_params']


def calculate_permutation_count(test_params, point_count):
    c = 0
    for f in test_params:
        for m in test_params[f]:
            for l, p in test_params[f][m].items():
                _c = 1
                for v in p['params'].values():
                    _c *= len(v)
                for v in p['ls_params'].values():
                    _c *= len(v)
                c += _c
    return c * point_count


best_params = {
    'MatrixSquareSum': {
        'NewtonsMethod': {
            # 'ConstantSearch': {
            #     'params': {'tolerance': 1e-4, 'max_iterations': 10000},  # noqa
            #     'ls_params': {'delta': 1},  # noqa
            # },
            # 'GoldenSectionSearch': {
            #     'params': {'tolerance': 1e-4, 'max_iterations': 10000},  # noqa
            #     'ls_params': {'a': -10, 'b': 5, 'tolerance': 1e-7, 'max_iterations': 10000},  # noqa
            # },
            # 'BisectionSearch': {
            #     'params': {'tolerance': 1e-4, 'max_iterations': 10000},  # noqa
            #     'ls_params': {'a': -10, 'b': 5, 'tolerance': 1e-7, 'max_iterations': 10000},  # noqa
            # },
            'DichotomousSearch': {
                'params': {'tolerance': 1e-4, 'max_iterations': 10000},  # noqa
                'ls_params': {'a': -5, 'b': 10, 'epsilon': 1e-10, 'tolerance': 1e-09, 'max_iterations': 10000},  # noqa
            },
            # 'FibonacciSearch': {
            #     'params': {'tolerance': 1e-4, 'max_iterations': 10000},  # noqa
            #     'ls_params': {'a': -5, 'b': 5, 'epsilon': 1e-10, 'tolerance': 1e-10, 'max_iterations': 10000},  # noqa
            # },
            # 'UniformSearch': {
            #     'params': {'tolerance': 1e-4, 'max_iterations': 10000},  # noqa
            #     'ls_params': {'a': -10, 'b': 5, 'interval_count': 5, 'interval_multiplier': 1.5, 'tolerance': 1e-6, 'max_iterations': 10000},  # noqa
            # },
            # 'NewtonsSearch': {
            #     'params': {'tolerance': 1e-4, 'max_iterations': 10000},  # noqa
            #     'ls_params': {'delta': 1, 'tolerance': 1e-7, 'max_iterations': 10000},  # noqa
            # },
            # 'ArmijoSearch': {
            #     'params': {'tolerance': 1e-4, 'max_iterations': 10000},  # noqa
            #     'ls_params': {'delta': 1, 'alpha': 0.1, 'beta': 0.5, 'max_iterations': 10000},  # noqa
            # },
        },
        # 'GradientDescentMethod': {
            # 'ConstantSearch': {
            #     'params': {'tolerance': 1e-4, 'max_iterations': 10000},  # noqa
            #     'ls_params': {'delta': 0.0001},  # noqa
            # },
            # 'GoldenSectionSearch': {
            #     'params': {'tolerance': 1e-4, 'max_iterations': 10000},  # noqa
            #     'ls_params': {'a': -10, 'b': 5, 'tolerance': 1e-4, 'max_iterations': 10000},  # noqa
            # },
            # 'BisectionSearch': {
            #     'params': {'tolerance': 1e-4, 'max_iterations': 10000},  # noqa
            #     'ls_params': {'a': -10, 'b': 5, 'tolerance': 1e-4, 'max_iterations': 10000},  # noqa
            # },
            # 'DichotomousSearch': {
            #     'params': {'tolerance': 1e-4, 'max_iterations': 10000},  # noqa
            #     'ls_params': {'a': -10, 'b': 5, 'epsilon': 1e-7, 'tolerance': 1e-5, 'max_iterations': 10000},  # noqa
            # },
            # 'FibonacciSearch': {
            #     'params': {'tolerance': 1e-4, 'max_iterations': 10000},  # noqa
            #     'ls_params': {'a': -5, 'b': 10, 'epsilon': 1e-12, 'tolerance': 1e-6, 'max_iterations': 10000},  # noqa
            # },
            # 'UniformSearch': {
            #     'params': {'tolerance': 1e-4, 'max_iterations': 10000},  # noqa
            #     'ls_params': {'a': -10, 'b': 5, 'interval_count': 5, 'interval_multiplier': 1, 'tolerance': 1e-6, 'max_iterations': 10000},  # noqa
            # },
            # 'NewtonsSearch': {
            #     'params': {'tolerance': 1e-4, 'max_iterations': 10000},  # noqa
            #     'ls_params': {'delta': 1, 'tolerance': 1e-8, 'max_iterations': 10000},  # noqa
            # },
            # 'ArmijoSearch': {
            #     'params': {'tolerance': 1e-4, 'max_iterations': 1000},  # noqa
            #     'ls_params': {'delta': 1.1, 'alpha': 0.25, 'beta': 0.5, 'max_iterations': 10000},  # noqa
            # },
        # },
        # 'ConjugateGradientMethod': {
            # 'ConstantSearch': {
            #     'params': {'tolerance': 1e-4, 'max_iterations': 10000},  # noqa
            #     'ls_params': {'delta': 0.0001},  # noqa
            # },
            # 'GoldenSectionSearch': {
            #     'params': {'tolerance': 1e-4, 'max_iterations': 10000},  # noqa
            #     'ls_params': {'a': -5, 'b': 10, 'tolerance': 1e-4, 'max_iterations': 10000},  # noqa
            # },
            # 'BisectionSearch': {
            #     'params': {'tolerance': 1e-4, 'max_iterations': 10000},  # noqa
            #     'ls_params': {'a': -10, 'b': 10, 'tolerance': 1e-4, 'max_iterations': 10000},  # noqa
            # },
            # 'DichotomousSearch': {
            #     'params': {'tolerance': 1e-4, 'max_iterations': 10000},  # noqa
            #     'ls_params': {'a': -5, 'b': 10, 'epsilon': 1e-7, 'tolerance': 1e-5, 'max_iterations': 10000},  # noqa
            # },
            # 'FibonacciSearch': {
            #     'params': {'tolerance': 1e-4, 'max_iterations': 10000},  # noqa
            #     'ls_params': {'a': -5, 'b': 10, 'epsilon': 1e-10, 'tolerance': 1e-6, 'max_iterations': 10000},  # noqa
            # },
            # 'UniformSearch': {
            #     'params': {'tolerance': 1e-4, 'max_iterations': 10000},  # noqa
            #     'ls_params': {'a': -5, 'b': 10, 'interval_count': 5, 'interval_multiplier': 1, 'tolerance': 1e-6, 'max_iterations': 10000},  # noqa
            # },
            # 'NewtonsSearch': {
            #     'params': {'tolerance': 1e-4, 'max_iterations': 10000},  # noqa
            #     'ls_params': {'delta': 1, 'tolerance': 1e-7, 'max_iterations': 10000},  # noqa
            # },
            # 'ArmijoSearch': {
            #     'params': {'tolerance': 1e-4, 'beta': 0.9, 'max_iterations': 10000},  # noqa
            #     'ls_params': {'delta': 1.1, 'alpha': 0.25, 'beta': 0.5, 'max_iterations': 10000},  # noqa
            # },
        # },
        # 'HeavyBallMethod': {
            # 'ConstantSearch': {
            #     'params': {'tolerance': 1e-4, 'beta': 0.1, 'max_iterations': 10000},  # noqa
            #     'ls_params': {'delta': 0.0001},  # noqa
            # },
            # 'GoldenSectionSearch': {
            #     'params': {'tolerance': 1e-4, 'beta': 10, 'max_iterations': 10000},  # noqa
            #     'ls_params': {'a': -5, 'b': 10, 'tolerance': 1e-4, 'max_iterations': 10000},  # noqa
            # },
            # 'BisectionSearch': {
            #     'params': {'tolerance': 1e-4, 'beta': 10, 'max_iterations': 10000},  # noqa
            #     'ls_params': {'a': -10, 'b': 10, 'tolerance': 1e-4, 'max_iterations': 10000},  # noqa
            # },
            # 'DichotomousSearch': {
            #     'params': {'tolerance': 1e-4, 'beta': 10, 'max_iterations': 10000},  # noqa
            #     'ls_params': {'a': -5, 'b': 5, 'epsilon': 1e-7, 'tolerance': 1e-4, 'max_iterations': 10000},  # noqa
            # },
            # 'FibonacciSearch': {
            #     'params': {'tolerance': 1e-4, 'beta': 0.5, 'max_iterations': 10000},  # noqa
            #     'ls_params': {'a': -10, 'b': 5, 'epsilon': 1e-12, 'tolerance': 1e-6, 'max_iterations': 10000},  # noqa
            # },
            # 'UniformSearch': {
            #     'params': {'tolerance': 1e-4, 'beta': 10, 'max_iterations': 10000},  # noqa
            #     'ls_params': {'a': -10, 'b': 10, 'interval_count': 5, 'interval_multiplier': 1, 'tolerance': 1e-6, 'max_iterations': 10000},  # noqa
            # },
            # 'NewtonsSearch': {
            #     'params': {'tolerance': 1e-4, 'beta': 10, 'max_iterations': 10000},  # noqa
            #     'ls_params': {'delta': 10, 'tolerance': 1e-7, 'max_iterations': 10000},  # noqa
            # },
            # 'ArmijoSearch': {
            #     'params': {'tolerance': 1e-4, 'beta': 0.1, 'max_iterations': 10000},  # noqa
            #     'ls_params': {'delta': 1.1, 'alpha': 0.25, 'beta': 0.5, 'max_iterations': 10000},  # noqa
            # },
    #     },
    # },
    # 'NegativeEntropy': {
    #     'NewtonsMethod': {
            # 'ConstantSearch': {
            #     'params': {'tolerance': 1e-4, 'max_iterations': 10000},  # noqa
            #     'ls_params': {'delta': 0.9},  # noqa
            # },
            # 'GoldenSectionSearch': {
            #     'params': {'tolerance': 1e-4, 'max_iterations': 10000},  # noqa
            #     'ls_params': {'a': -5, 'b': 5, 'tolerance': 1e-7, 'max_iterations': 10000},  # noqa
            # },
            # 'BisectionSearch': {
            #     'params': {'tolerance': 1e-4, 'max_iterations': 10000},  # noqa
            #     'ls_params': {'a': -10, 'b': 10, 'tolerance': 1e-4, 'max_iterations': 10000},  # noqa
            # },
            # 'DichotomousSearch': {
            #     'params': {'tolerance': 1e-4, 'max_iterations': 10000},  # noqa
            #     'ls_params': {'a': -10, 'b': 10, 'epsilon': 1e-7, 'tolerance': 1e-5, 'max_iterations': 10000},  # noqa
            # },
            # 'FibonacciSearch': {
            #     'params': {'tolerance': 1e-4, 'max_iterations': 10000},  # noqa
            #     'ls_params': {'a': -5, 'b': 5, 'epsilon': 1e-12, 'tolerance': 1e-12, 'max_iterations': 10000},  # noqa
            # },
            # 'UniformSearch': {
            #     'params': {'tolerance': 1e-4, 'max_iterations': 10000},  # noqa
            #     'ls_params': {'a': 0, 'b': 5, 'interval_count': 5, 'interval_multiplier': 1, 'tolerance': 1e-5, 'max_iterations': 10000},  # noqa
            # },
            # 'NewtonsSearch': {
            #     'params': {'tolerance': 1e-4, 'max_iterations': 10000},  # noqa
            #     'ls_params': {'delta': 0.5, 'tolerance': 1e-8, 'max_iterations': 100},  # noqa
            # },
            # 'ArmijoSearch': {
            #     'params': {'tolerance': 1e-4, 'max_iterations': 10000},  # noqa
            #     'ls_params': {'delta': 1.1, 'alpha': 0.5, 'beta': 0.9, 'max_iterations': 10000},  # noqa
            # },
        # },
        # 'GradientDescentMethod': {
            # 'ConstantSearch': {
            #     'params': {'tolerance': 1e-4, 'max_iterations': 10000},  # noqa
            #     'ls_params': {'delta': 0.5},  # noqa
            # },
            # 'GoldenSectionSearch': {
            #     'params': {'tolerance': 1e-4, 'max_iterations': 10000},  # noqa
            #     'ls_params': {'a': -5, 'b': 5, 'tolerance': 1e-4, 'max_iterations': 10000},  # noqa
            # },
            # 'BisectionSearch': {
            #     'params': {'tolerance': 1e-4, 'max_iterations': 10000},  # noqa
            #     'ls_params': {'a': -5, 'b': 5, 'tolerance': 1e-4, 'max_iterations': 10000},  # noqa
            # },
            # 'DichotomousSearch': {
            #     'params': {'tolerance': 1e-4, 'max_iterations': 10000},  # noqa
            #     'ls_params': {'a': -5, 'b': 5, 'epsilon': 1e-7, 'tolerance': 1e-4, 'max_iterations': 10000},  # noqa
            # },
            # 'FibonacciSearch': {
            #     'params': {'tolerance': 1e-4, 'max_iterations': 10000},  # noqa
            #     'ls_params': {'a': -5, 'b': 5, 'epsilon': 1e-12, 'tolerance': 1e-6, 'max_iterations': 10000},  # noqa
            # },
            # 'UniformSearch': {
            #     'params': {'tolerance': 1e-4, 'max_iterations': 10000},  # noqa
            #     'ls_params': {'a': 0, 'b': 5, 'interval_count': 10, 'interval_multiplier': 1, 'tolerance': 1e-5, 'max_iterations': 10000},  # noqa
            # },
            # 'NewtonsSearch': {
            #     'params': {'tolerance': 1e-4, 'max_iterations': 10000},  # noqa
            #     'ls_params': {'delta': 0.5, 'tolerance': 1e-7, 'max_iterations': 100},  # noqa
            # },
            # 'ArmijoSearch': {
            #     'params': {'tolerance': 1e-4, 'max_iterations': 10000},  # noqa
            #     'ls_params': {'delta': 1.1, 'alpha': 0.5, 'beta': 0.75, 'max_iterations': 10000},  # noqa
            # },
        # },
        # 'ConjugateGradientMethod': {
            # 'ConstantSearch': {
            #     'params': {'tolerance': 1e-4, 'max_iterations': 10000},  # noqa
            #     'ls_params': {'delta': 0.1},  # noqa
            # },
            # 'GoldenSectionSearch': {
            #     'params': {'tolerance': 1e-4, 'max_iterations': 10000},  # noqa
            #     'ls_params': {'a': -5, 'b': 5, 'tolerance': 1e-4, 'max_iterations': 10000},  # noqa
            # },
            # 'BisectionSearch': {
            #     'params': {'tolerance': 1e-4, 'max_iterations': 10000},  # noqa
            #     'ls_params': {'a': -5, 'b': 5, 'tolerance': 1e-4, 'max_iterations': 10000},  # noqa
            # },
            # 'DichotomousSearch': {
            #     'params': {'tolerance': 1e-4, 'max_iterations': 10000},  # noqa
            #     'ls_params': {'a': -5, 'b': 5, 'epsilon': 1e-6, 'tolerance': 1e-4, 'max_iterations': 10000},  # noqa
            # },
            # 'FibonacciSearch': {
            #     'params': {'tolerance': 1e-4, 'max_iterations': 10000},  # noqa
            #     'ls_params': {'a': -5, 'b': 5, 'epsilon': 1e-8, 'tolerance': 1e-6, 'max_iterations': 10000},  # noqa
            # },
            # 'UniformSearch': {
            #     'params': {'tolerance': 1e-4, 'max_iterations': 10000},  # noqa
            #     'ls_params': {'a': 0, 'b': 5, 'interval_count': 10, 'interval_multiplier': 1, 'tolerance': 1e-5, 'max_iterations': 10000},  # noqa
            # },
            # 'NewtonsSearch': {
            #     'params': {'tolerance': 1e-4, 'max_iterations': 10000},  # noqa
            #     'ls_params': {'delta': 0.1, 'tolerance': 1e-8, 'max_iterations': 100},  # noqa
            # },
            # 'ArmijoSearch': {
            #     'params': {'tolerance': 1e-4, 'max_iterations': 10000},  # noqa
            #     'ls_params': {'delta': 0.9, 'alpha': 0.5, 'beta': 0.5, 'max_iterations': 10000},  # noqa
            # },
        # },
        # 'HeavyBallMethod': {
            # 'ConstantSearch': {
            #     'params': {'tolerance': 1e-4, 'beta': 0.1, 'max_iterations': 10000},  # noqa
            #     'ls_params': {'delta': 0.5},  # noqa
            # },
            # 'GoldenSectionSearch': {
            #     'params': {'tolerance': 1e-4, 'beta': 0.5, 'max_iterations': 10000},  # noqa
            #     'ls_params': {'a': -5, 'b': 5, 'tolerance': 1e-4, 'max_iterations': 10000},  # noqa
            # },
            # 'BisectionSearch': {
            #     'params': {'tolerance': 1e-4, 'beta': 0.1, 'max_iterations': 10000},  # noqa
            #     'ls_params': {'a': -10, 'b': 10, 'tolerance': 1e-4, 'max_iterations': 10000},  # noqa
            # },
            # 'DichotomousSearch': {
            #     'params': {'tolerance': 1e-4, 'beta': 0.1, 'max_iterations': 10000},  # noqa
            #     'ls_params': {'a': -5, 'b': 5, 'epsilon': 1e-6, 'tolerance': 1e-5, 'max_iterations': 10000},  # noqa
            # },
            # 'FibonacciSearch': {
            #     'params': {'tolerance': 1e-4, 'beta': 0.1, 'max_iterations': 10000},  # noqa
            #     'ls_params': {'a': -5, 'b': 5, 'epsilon': 1e-12, 'tolerance': 1e-6, 'max_iterations': 10000},  # noqa
            # },
            # 'UniformSearch': {
            #     'params': {'tolerance': 1e-4, 'beta': 0.1, 'max_iterations': 10000},  # noqa
            #     'ls_params': {'a': 0, 'b': 5, 'interval_count': 10, 'interval_multiplier': 1, 'tolerance': 1e-5, 'max_iterations': 10000},  # noqa
            # },
            # 'NewtonsSearch': {
            #     'params': {'tolerance': 1e-4, 'beta': 0.1, 'max_iterations': 10000},  # noqa
            #     'ls_params': {'delta': 1, 'tolerance': 1e-7, 'max_iterations': 100},  # noqa
            # },
            # 'ArmijoSearch': {
            #     'params': {'tolerance': 1e-4, 'beta': 0.1, 'max_iterations': 10000},  # noqa
            #     'ls_params': {'delta': 1, 'alpha': 0.5, 'beta': 0.5, 'max_iterations': 10000},  # noqa
            # },
    #     },
    },
}

# visualization_params = {
#     **best_params['MatrixSquareSum'],
# }

test_params2 = {
    'MatrixSquareSum': {
        'NewtonsMethod': {
            'ConstantSearch': {
                'params': {'tolerance': [1e-6], 'max_iterations': [10000]},  # noqa
                'ls_params': {'delta': [0.0001, 0.1, 0.25, 0.5, 0.9]},  # noqa
            },
            'GoldenSectionSearch': {
                'params': {'tolerance': [1e-6], 'max_iterations': [10000]},  # noqa
                'ls_params': {'a': [-10, -5], 'b': [10, 5], 'tolerance': [1e-4, 1e-7], 'max_iterations': [10000]},  # noqa
            },
            'BisectionSearch': {
                'params': {'tolerance': [1e-6], 'max_iterations': [10000]},  # noqa
                'ls_params': {'a': [-10, -5], 'b': [10, 5], 'tolerance': [1e-4, 1e-7], 'max_iterations': [10000]},  # noqa
            },
            'DichotomousSearch': {
                'params': {'tolerance': [1e-6], 'max_iterations': [10000]},  # noqa
                'ls_params': {'a': [-10, -5], 'b': [10, 5], 'epsilon': [1e-2, 1e-5, 1e-8], 'tolerance': [1e-4], 'max_iterations': [10000]},  # noqa
            },
            'FibonacciSearch': {
                'params': {'tolerance': [1e-6], 'max_iterations': [10000]},  # noqa
                'ls_params': {'a': [-10, -5], 'b': [10, 5], 'epsilon': [1e-2, 1e-5, 1e-8], 'tolerance': [1e-4, 1e-7], 'max_iterations': [10000]},  # noqa
            },
            'UniformSearch': {
                'params': {'tolerance': [1e-6], 'max_iterations': [10000]},  # noqa
                'ls_params': {'a': [-10, -5], 'b': [10, 5], 'interval_count': [10, 100], 'interval_multiplier': [1, 1.5], 'tolerance': [1e-4, 1e-7], 'max_iterations': [10000]},  # noqa
            },
            'NewtonsSearch': {
                'params': {'tolerance': [1e-6], 'max_iterations': [10000]},  # noqa
                'ls_params': {'delta': [0.0001, 0.1, 0.25, 0.5, 0.9, 1, 1.5], 'tolerance': [1e-4, 1e-7], 'max_iterations': [10000]},  # noqa
            },
            'ArmijoSearch': {
                'params': {'tolerance': [1e-6], 'max_iterations': [10000]},  # noqa
                'ls_params': {'delta': [0.1, 0.25, 0.5, 0.9], 'alpha': [0.1, 0.25, 0.5, 0.75, 0.9], 'beta': [0.1, 0.25, 0.5, 0.75, 0.9], 'tolerance': [1e-6], 'max_iterations': [10000]},  # noqa
            },
        },
        'GradientDescentMethod': {
            'ConstantSearch': {
                'params': {'tolerance': [1e-6], 'max_iterations': [10000]},  # noqa
                'ls_params': {'delta': [0.25, 0.5, 0.75, 0.9, 1, 1.1]},  # noqa
            },
            'GoldenSectionSearch': {
                'params': {'tolerance': [1e-6], 'max_iterations': [1000]},  # noqa
                'ls_params': {'a': [-10], 'b': [10], 'tolerance': [1e-6], 'max_iterations': [1000]},  # noqa
            },
            'BisectionSearch': {
                'params': {'tolerance': [1e-6], 'max_iterations': [1000]},  # noqa
                'ls_params': {'a': [-10], 'b': [10], 'tolerance': [1e-6], 'max_iterations': [1000]},  # noqa
            },
            'DichotomousSearch': {
                'params': {'tolerance': [1e-6], 'max_iterations': [1000]},  # noqa
                'ls_params': {'a': [-10], 'b': [10], 'epsilon': [1e-3, 1e-6, 1e-9], 'tolerance': [1e-4], 'max_iterations': [100]},  # noqa
            },
            'FibonacciSearch': {
                'params': {'tolerance': [1e-6], 'max_iterations': [1000]},  # noqa
                'ls_params': {'a': [-10], 'b': [10], 'epsilon': [1e-3, 1e-6, 1e-9], 'tolerance': [1e-6], 'max_iterations': [1000]},  # noqa
            },
            'UniformSearch': {
                'params': {'tolerance': [1e-6], 'max_iterations': [100]},  # noqa
                'ls_params': {'a': [-10], 'b': [10], 'interval_count': [10, 100], 'interval_multiplier': [1, 1.5], 'tolerance': [1e-6], 'max_iterations': [100]},  # noqa
            },
            'NewtonsSearch': {
                'params': {'tolerance': [1e-6], 'max_iterations': [1000]},  # noqa
                'ls_params': {'delta': [0, 0.5, 1, 5, 8, 10], 'tolerance': [1e-6], 'max_iterations': [1000]},  # noqa
            },
            'ArmijoSearch': {
                'params': {'tolerance': [1e-6], 'max_iterations': [10000]},  # noqa
                'ls_params': {'delta': [0.1, 0.25, 0.5, 0.9], 'alpha': [0.1, 0.25, 0.5, 0.75, 0.9], 'beta': [0.1, 0.25, 0.5, 0.75, 0.9], 'tolerance': [1e-6], 'max_iterations': [10000]},  # noqa
            },
        },
        'ConjugateGradientMethod': {
            'ConstantSearch': {
                'params': {'tolerance': [1e-6], 'max_iterations': [10000]},  # noqa
                'ls_params': {'delta': [0.25, 0.5, 0.75, 0.9, 1, 1.1]},  # noqa
            },
            'GoldenSectionSearch': {
                'params': {'tolerance': [1e-6], 'max_iterations': [1000]},  # noqa
                'ls_params': {'a': [-10], 'b': [10], 'tolerance': [1e-6], 'max_iterations': [1000]},  # noqa
            },
            'BisectionSearch': {
                'params': {'tolerance': [1e-6], 'max_iterations': [1000]},  # noqa
                'ls_params': {'a': [-10], 'b': [10], 'tolerance': [1e-6], 'max_iterations': [1000]},  # noqa
            },
            'DichotomousSearch': {
                'params': {'tolerance': [1e-6], 'max_iterations': [1000]},  # noqa
                'ls_params': {'a': [-10], 'b': [10], 'epsilon': [1e-3, 1e-6, 1e-9], 'tolerance': [1e-4], 'max_iterations': [100]},  # noqa
            },
            'FibonacciSearch': {
                'params': {'tolerance': [1e-6], 'max_iterations': [1000]},  # noqa
                'ls_params': {'a': [-10], 'b': [10], 'epsilon': [1e-3, 1e-6, 1e-9], 'tolerance': [1e-6], 'max_iterations': [1000]},  # noqa
            },
            'UniformSearch': {
                'params': {'tolerance': [1e-6], 'max_iterations': [100]},  # noqa
                'ls_params': {'a': [-10], 'b': [10], 'interval_count': [10, 100], 'interval_multiplier': [1, 1.5], 'tolerance': [1e-6], 'max_iterations': [100]},  # noqa
            },
            'NewtonsSearch': {
                'params': {'tolerance': [1e-6], 'max_iterations': [1000]},  # noqa
                'ls_params': {'delta': [0, 0.5, 1, 5, 8, 10], 'tolerance': [1e-6], 'max_iterations': [1000]},  # noqa
            },
            'ArmijoSearch': {
                'params': {'tolerance': [1e-6], 'max_iterations': [10000]},  # noqa
                'ls_params': {'delta': [0.1, 0.25, 0.5, 0.9], 'alpha': [0.1, 0.25, 0.5, 0.75, 0.9], 'beta': [0.1, 0.25, 0.5, 0.75, 0.9], 'tolerance': [1e-6], 'max_iterations': [10000]},  # noqa
            },
        },
        'HeavyBallMethod': {
            'ConstantSearch': {
                'params': {'tolerance': [1e-6], 'beta': [0.01, 0.1, 0.25, 0.5], 'max_iterations': [10000]},  # noqa
                'ls_params': {'delta': [0.25, 0.5, 0.75, 0.9, 1, 1.1, ]},  # noqa
            },
            'GoldenSectionSearch': {
                'params': {'tolerance': [1e-6], 'beta': [0.01, 0.1, 0.25, 0.5], 'max_iterations': [1000]},  # noqa
                'ls_params': {'a': [-10], 'b': [10], 'tolerance': [1e-6], 'max_iterations': [1000]},  # noqa
            },
            'BisectionSearch': {
                'params': {'tolerance': [1e-6], 'beta': [0.01, 0.1, 0.25, 0.5], 'max_iterations': [1000]},  # noqa
                'ls_params': {'a': [-10], 'b': [10], 'tolerance': [1e-6], 'max_iterations': [1000]},  # noqa
            },
            'DichotomousSearch': {
                'params': {'tolerance': [1e-6], 'beta': [0.01, 0.1, 0.25, 0.5], 'max_iterations': [1000]},  # noqa
                'ls_params': {'a': [-10], 'b': [10], 'epsilon': [1e-3, 1e-6, 1e-9], 'tolerance': [1e-4], 'max_iterations': [100]},  # noqa
            },
            'FibonacciSearch': {
                'params': {'tolerance': [1e-6], 'beta': [0.01, 0.1, 0.25, 0.5], 'max_iterations': [1000]},  # noqa
                'ls_params': {'a': [-10], 'b': [10], 'epsilon': [1e-3, 1e-6, 1e-9], 'tolerance': [1e-6], 'max_iterations': [1000]},  # noqa
            },
            'UniformSearch': {
                'params': {'tolerance': [1e-6], 'beta': [0.01, 0.1, 0.25, 0.5], 'max_iterations': [100]},  # noqa
                'ls_params': {'a': [-10], 'b': [10], 'interval_count': [10, 100], 'interval_multiplier': [1, 1.5], 'tolerance': [1e-6], 'max_iterations': [100]},  # noqa
            },
            'NewtonsSearch': {
                'params': {'tolerance': [1e-6], 'beta': [0.01, 0.1, 0.25, 0.5], 'max_iterations': [1000]},  # noqa
                'ls_params': {'delta': [0, 0.5, 1, 5, 8, 10], 'tolerance': [1e-6], 'max_iterations': [1000]},  # noqa
            },
            'ArmijoSearch': {
                'params': {'tolerance': [1e-6], 'beta': [0.1, 0.5, 0.9], 'max_iterations': [10000]},  # noqa
                'ls_params': {'delta': [0.1, 0.25, 0.5, 0.9], 'alpha': [0.1, 0.25, 0.5, 0.9], 'beta': [0.1, 0.25, 0.5, 0.9], 'tolerance': [1e-6], 'max_iterations': [10000]},  # noqa
            },
        },
    },
    # 'NegativeEntropy': {
        # 'NewtonsMethod': {
        #     'ConstantSearch': {
        #         'params': {'tolerance': [1e-8], 'max_iterations': [10000]},  # noqa
        #         'ls_params': {'delta': [0.25, 0.5, 0.75, 0.9, 1, 1.1, 1.5]},  # noqa
        #     },
            # 'GoldenSectionSearch': {
            #     'params': {'tolerance': [1e-8], 'max_iterations': [1000]},  # noqa
            #     'ls_params': {'a': [0.1, 0.5], 'b': [10, 5], 'tolerance': [1e-6], 'max_iterations': [1000]},  # noqa
            # },
        #     'BisectionSearch': {
        #         'params': {'tolerance': [1e-8], 'max_iterations': [1000]},  # noqa
        #         'ls_params': {'a': [0.1, 0.5, 1, 2], 'b': [10, 5], 'tolerance': [1e-6], 'max_iterations': [1000]},  # noqa
        #     },
        #     'DichotomousSearch': {
        #         'params': {'tolerance': [1e-4], 'max_iterations': [1000]},  # noqa
        #         'ls_params': {'a': [0.1, 0.5], 'b': [10, 5], 'epsilon': [1e-3, 1e-6, 1e-9], 'tolerance': [1e-4], 'max_iterations': [1000]},  # noqa
        #     },
        #     'FibonacciSearch': {
        #         'params': {'tolerance': [1e-8], 'max_iterations': [1000]},  # noqa
        #         'ls_params': {'a': [0.1, 0.5], 'b': [10, 5], 'epsilon': [1e-3, 1e-6, 1e-9], 'tolerance': [1e-6], 'max_iterations': [1000]},  # noqa
        #     },
        #     'UniformSearch': {
        #         'params': {'tolerance': [1e-8], 'max_iterations': [0]},  # noqa
        #         'ls_params': {'a': [1], 'b': [10, 5], 'interval_count': [10, 100], 'interval_multiplier': [1, 1.5], 'tolerance': [1e-6], 'max_iterations': [100]},  # noqa
        #     },
        #     'NewtonsSearch': {
        #         'params': {'tolerance': [1e-8], 'max_iterations': [0]},  # noqa
        #         'ls_params': {'delta': [0, 0.5, 1, 5], 'tolerance': [1e-6], 'max_iterations': [1000]},  # noqa
        #     },
            # 'ArmijoSearch': {
            #     'params': {'tolerance': [1e-5], 'max_iterations': [10000]},  # noqa
            #     'ls_params': {'delta': [0.1, 0.25, 0.5, 0.9], 'alpha': [0.1, 0.25, 0.5, 0.75, 0.9], 'beta': [0.1, 0.25, 0.5, 0.75, 0.9], 'tolerance': [1e-6], 'max_iterations': [10000]},  # noqa
            # },
        # },
        # 'GradientDescentMethod': {
            # 'ConstantSearch': {
            #     'params': {'tolerance': [1e-8], 'max_iterations': [10000]},  # noqa
            #     'ls_params': {'delta': [0.25, 0.5, 0.75, 0.9, 1, 1.1,]},  # noqa
            # },
            # 'GoldenSectionSearch': {
            #     'params': {'tolerance': [1e-8], 'max_iterations': [1000]},  # noqa
            #     'ls_params': {'a': [0.5], 'b': [10], 'tolerance': [1e-6], 'max_iterations': [1000]},  # noqa
            # },
            # 'BisectionSearch': {
            #     'params': {'tolerance': [1e-8], 'max_iterations': [1000]},  # noqa
            #     'ls_params': {'a': [0.5], 'b': [10], 'tolerance': [1e-6], 'max_iterations': [1000]},  # noqa
            # },
            # 'DichotomousSearch': {
            #     'params': {'tolerance': [1e-4], 'max_iterations': [1000]},  # noqa
            #     'ls_params': {'a': [0.5], 'b': [10], 'epsilon': [1e-3, 1e-6, 1e-9], 'tolerance': [1e-4], 'max_iterations': [100]},  # noqa
            # },
            # 'FibonacciSearch': {
            #     'params': {'tolerance': [1e-8], 'max_iterations': [1000]},  # noqa
            #     'ls_params': {'a': [0.5], 'b': [10], 'epsilon': [1e-3, 1e-6, 1e-9], 'tolerance': [1e-6], 'max_iterations': [1000]},  # noqa
            # },
            # 'UniformSearch': {
            #     'params': {'tolerance': [1e-8], 'max_iterations': [1000]},  # noqa
            #     'ls_params': {'a': [0.5], 'b': [10], 'interval_count': [10, 100], 'interval_multiplier': [1, 1.5], 'tolerance': [1e-6], 'max_iterations': [100]},  # noqa
            # },
            # 'NewtonsSearch': {
            #     'params': {'tolerance': [1e-8], 'max_iterations': [1000]},  # noqa
            #     'ls_params': {'delta': [0, 0.5, 1, 5, 8, 10], 'tolerance': [1e-6], 'max_iterations': [100]},  # noqa
            # },
            # 'ArmijoSearch': {
            #     'params': {'tolerance': [1e-5], 'max_iterations': [10000]},  # noqa
            #     'ls_params': {'delta': [0.1, 0.25, 0.5, 0.9], 'alpha': [0.1, 0.25, 0.5, 0.75, 0.9], 'beta': [0.1, 0.25, 0.5, 0.75, 0.9], 'tolerance': [1e-6], 'max_iterations': [10000]},  # noqa
            # },
        # },
        # 'ConjugateGradientMethod': {
        #     'ConstantSearch': {
        #         'params': {'tolerance': [1e-8], 'max_iterations': [1000]},  # noqa
        #         'ls_params': {'delta': [0, 0.1, 0.25, 1, 1.5, 3]},  # noqa
        #     },
            # 'GoldenSectionSearch': {
            #     'params': {'tolerance': [1e-8], 'max_iterations': [1000]},  # noqa
            #     'ls_params': {'a': [-1, 0, 0.1], 'b': [10], 'tolerance': [1e-6], 'max_iterations': [1000]},  # noqa
            # },
            # 'BisectionSearch': {
            #     'params': {'tolerance': [1e-8], 'max_iterations': [1000]},  # noqa
            #     'ls_params': {'a': [-1, 0, 0.1], 'b': [10], 'tolerance': [1e-6], 'max_iterations': [1000]},  # noqa
            # },
            # 'DichotomousSearch': {
            #     'params': {'tolerance': [1e-4], 'max_iterations': [1000]},  # noqa
            #     'ls_params': {'a': [-1, 0, 0.1], 'b': [10], 'epsilon': [1e-3, 1e-6, 1e-9], 'tolerance': [1e-4], 'max_iterations': [100]},  # noqa
            # },
            # 'FibonacciSearch': {
            #     'params': {'tolerance': [1e-8], 'max_iterations': [1000]},  # noqa
            #     'ls_params': {'a': [-1, 0, 0.1], 'b': [10], 'epsilon': [1e-3, 1e-6, 1e-9], 'tolerance': [1e-6], 'max_iterations': [1000]},  # noqa
            # },
            # 'UniformSearch': {
            #     'params': {'tolerance': [1e-8], 'max_iterations': [1000]},  # noqa
            #     'ls_params': {'a': [0.5], 'b': [10], 'interval_count': [10], 'interval_multiplier': [1.5], 'tolerance': [1e-6], 'max_iterations': [100]},  # noqa
            # },
            # 'NewtonsSearch': {
            #     'params': {'tolerance': [1e-8], 'max_iterations': [1000]},  # noqa
            #     'ls_params': {'delta': [0, 0.5, 1, 5, 8, 10], 'tolerance': [1e-6], 'max_iterations': [1000]},  # noqa
            # },
            # 'ArmijoSearch': {
            #     'params': {'tolerance': [1e-5], 'max_iterations': [10000]},  # noqa
            #     'ls_params': {'delta': [0.1, 0.25, 0.5, 0.9], 'alpha': [0.1, 0.25, 0.5, 0.75, 0.9], 'beta': [0.1, 0.25, 0.5, 0.75, 0.9], 'tolerance': [1e-6], 'max_iterations': [10000]},  # noqa
            # },
        # },
        # 'HeavyBallMethod': {
    #        'ConstantSearch': {
    #             'params': {'tolerance': [1e-8], 'beta': [0.1, 0.5, 0.75], 'max_iterations': [10000]},  # noqa
    #             'ls_params': {'delta': [0.25, 0.5, 0.75, 0.9, 1, 1.1,]},  # noqa
    #         },
    #         'GoldenSectionSearch': {
    #             'params': {'tolerance': [1e-8], 'beta': [0.1, 0.5, 0.75], 'max_iterations': [1000]},  # noqa
    #             'ls_params': {'a': [0.5], 'b': [10], 'tolerance': [1e-6], 'max_iterations': [1000]},  # noqa
    #         },
    #         'BisectionSearch': {
    #             'params': {'tolerance': [1e-8], 'beta': [0.1, 0.5, 0.75], 'max_iterations': [1000]},  # noqa
    #             'ls_params': {'a': [0.5], 'b': [10], 'tolerance': [1e-6], 'max_iterations': [1000]},  # noqa
    #         },
    #         'DichotomousSearch': {
    #             'params': {'tolerance': [1e-4], 'beta': [0.1, 0.5, 0.75], 'max_iterations': [1000]},  # noqa
    #             'ls_params': {'a': [0.5], 'b': [10], 'epsilon': [1e-3, 1e-6, 1e-9], 'tolerance': [1e-4], 'max_iterations': [100]},  # noqa
    #         },
    #         'FibonacciSearch': {
    #             'params': {'tolerance': [1e-8], 'beta': [0.1, 0.5, 0.75], 'max_iterations': [1000]},  # noqa
    #             'ls_params': {'a': [0.5], 'b': [10], 'epsilon': [1e-3, 1e-6, 1e-9], 'tolerance': [1e-6], 'max_iterations': [1000]},  # noqa
    #         },
    #         'UniformSearch': {
    #             'params': {'tolerance': [1e-8], 'beta': [0.1, 0.5, 0.75], 'max_iterations': [100]},  # noqa
    #             'ls_params': {'a': [0.5], 'b': [10], 'interval_count': [10, 100], 'interval_multiplier': [1, 1.5], 'tolerance': [1e-6], 'max_iterations': [100]},  # noqa
    #         },
    #         'NewtonsSearch': {
    #             'params': {'tolerance': [1e-8], 'beta': [0.1, 0.5, 0.75], 'max_iterations': [100]},  # noqa
    #             'ls_params': {'delta': [0, 0.5, 1, 5, 8, 10], 'tolerance': [1e-6], 'max_iterations': [100]},  # noqa
    #         },
    #         'ArmijoSearch': {
    #             'params': {'tolerance': [1e-5], 'beta': [0.1, 0.5, 0.9], 'max_iterations': [10000]},  # noqa
    #             'ls_params': {'delta': [0.1, 0.25, 0.5, 0.9], 'alpha': [0.1, 0.25, 0.5, 0.9], 'beta': [0.1, 0.25, 0.5, 0.9], 'tolerance': [1e-6], 'max_iterations': [10000]},  # noqa
    #         },
    #     },
    # },
}
