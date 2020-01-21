import matplotlib.pyplot as plt
# import numpy as np

# theta_name = 'MatrixSquareSum'
theta_name = 'NegativeEntropy'
line_search_name = 'ArmijoSearch'
line_search_names = [
    'ConstantSearch',
    'GoldenSectionSearch',
    'BisectionSearch',
    'DichotomousSearch',
    'FibonacciSearch',
    'UniformSearch',
    'NewtonsSearch',
    'ArmijoSearch',
]
line_search_abbrs = [
    'CS',
    'GSS',
    'BS',
    'DS',
    'FS',
    'US',
    'NS',
    'AS'
]
main_method_names = [
    'NewtonsMethod',
    'ConjugateGradientMethod',
    'GradientDescentMethod',
    'HeavyBallMethod',
]

duration_data = {mmn: {lsn: [] for lsn in line_search_names}
                 for mmn in main_method_names}

for mmn in main_method_names:
    for lsn in line_search_names:
        filename = f'raw_{theta_name}_{mmn}_{lsn}.csv'
        with open(f'data/raw_performances/{filename}', 'r') as f:
            full = f.read()
            for row in full.split('\n'):
                if not len(row) > 1:
                    continue
                cols = row.split(';')
                duration_data[mmn][lsn].append(float(cols[2]))


fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(13, 11))
plt.setp(axes, xticks=[], xticklabels=line_search_abbrs,
         xlabel='Line Search Method', ylabel='Duration (ms)')

for i, mmn in enumerate(main_method_names):
    ax = axes[i % 2, i // 2]
    plt.sca(ax)
    plt.boxplot(duration_data[mmn].values(), 0, '', whis=[2.5, 97.5])
    ax.set_yscale('log')
    plt.title(mmn)

plt.suptitle(theta_name)
plt.show()
