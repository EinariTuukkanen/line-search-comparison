import numpy as np

from line_search_methods import line_search_dict
from main_methods import main_method_dict
from config import simple_test_params

MAIN_METHOD_ORDER = {
    'NewtonsMethod': 0,
    'GradientDescentMethod': 1,
    'ConjugateGradientMethod': 2,
    'HeavyBallMethod': 3
}

FIGURE_TEMPLATE = """\\begin{{figure}}[H]
\\captionof{{figure}}{{Best parameter permutations for different main methods using {line_search_name} for optimizing the {theta_name} function with {n} sample points.}}
\\label{{fig:param_comp_{theta_name}_{line_search_name}}}
{subfigures}
\\end{{figure}}"""  # noqa


SUBFIGURE_TEMPLATE = """\\begin{{subfigure}}[ht]{{.5\\textwidth}}
\\rowcolors{{2}}{{white}}{{gray!5}}
\\begin{{tabular}}{{|c|c|c|}}
\\hline
\\rowcolor{{gray!25}}
\\multicolumn{{3}}{{|c|}}{{{main_method_name}}} \\\\
\\hline
\\rowcolor{{gray!25}}
{subheader} \\\\
\\hline
{data}
\\hline
\\end{{tabular}}
\\caption{{Top 5 permutations with {main_method_name}}}
\\label{{subfig:param_comp_{theta_name}_{main_method_name}_{line_search_name}}}
\\end{{subfigure}}"""


PARAMETER_TABLE_TEMPLATE = """\\begin{{center}}
\\rowcolors{{2}}{{white}}{{gray!5}}
\\captionof{{table}}{{Parameters tested for {line_search_name}}}
\\label{{tab:params_{line_search_name}}}
\\begin{{tabular}}{{|c|c|c|}}
\\hline
\\rowcolor{{gray!25}}
{header} \\\\
\\hline
{data}
\\hline
\\end{{tabular}}
\\end{{center}}"""


def export_parameter_comparison_latex(result_dict, point_count):
    ls_names = []
    for i in result_dict.values():
        for j in i.values():
            for k in j:
                if k not in ls_names:
                    ls_names.append(k)
    for ls_name in ls_names:
        with open(f'latex/{ls_name}.tex', 'w') as f:
            f.write(generate_param_table(simple_test_params, ls_name))
            for theta_name in simple_test_params:
                f.write('\n\n')
                f.write(generate_figure(
                    result_dict, point_count, theta_name, ls_name
                ))


def generate_figure(result_dict, point_count, theta_name, line_search_name):
    subfigures = [
        generate_subfigure(result_dict, theta_name, mm_name, line_search_name)
        for mm_name in sorted(
            result_dict[theta_name], key=lambda k: MAIN_METHOD_ORDER[k]
        )
    ]

    return FIGURE_TEMPLATE.format(
        n=point_count,
        theta_name=theta_name,
        line_search_name=line_search_name,
        subfigures='\n\\hfill\n'.join(subfigures)
    )


def generate_subfigure(
        result_dict, theta_name, main_method_name, line_search_name):
    data_rows = [[]]
    s, t = [], []
    for result in sorted(
            result_dict[theta_name][main_method_name][line_search_name])[:5]:
        p1, p2 = result.get_optimized_params()
        p = str(tuple([*p2.values(), *p1.values()]))
        if p not in data_rows[0]:
            data_rows[0].append(p)
        s.append(result.success_rate())
        t.append(result.performance['main_method']['duration'] / result.m())
    data_rows.append(np.around(np.array(s), 1).reshape(len(s), 1))
    data_rows.append(np.around(np.array(t), 1).reshape(len(t), 1))
    data_rows[0] = np.array(data_rows[0]).reshape(len(data_rows[0]), 1)

    ls_cls = line_search_dict[line_search_name]
    mm_cls = main_method_dict[main_method_name]
    symbols = ','.join([
        *ls_cls.param_symbols.values(), *mm_cls.param_symbols.values()
    ])
    subheader = [f"$({symbols})$", '$s$ (\\%)', '$t$ (ms)']
    data = np.column_stack(data_rows)
    return SUBFIGURE_TEMPLATE.format(
        theta_name=theta_name,
        line_search_name=line_search_name,
        main_method_name=main_method_name,
        subheader=' & '.join(subheader),
        data='\n'.join([' & '.join(row) + ' \\\\' for row in data]),
    )


def generate_param_table(params, line_search_name):
    header = ['Parameter']
    param_names = []
    columns = []
    ls_cls = line_search_dict[line_search_name]
    for theta_name in params:
        header.append(theta_name)
        column = []
        ls_params = params[theta_name]['ls_params'][line_search_name]
        for key, values in ls_params.items():
            if key not in ls_cls.param_symbols:
                continue
            param_name = f'${ls_cls.param_symbols.get(key, key)}$'
            if param_name not in param_names:
                param_names.append(param_name)
            column.append(', '.join([str(i) for i in values]))
        columns.append(column)
    data = np.column_stack([param_names, *columns])
    return PARAMETER_TABLE_TEMPLATE.format(
        theta_name=theta_name,
        line_search_name=line_search_name,
        header=' & '.join(header),
        data='\n'.join([' & '.join(row) + ' \\\\' for row in data]),
    )


PERFORMANCE_TABLE_TEMPLATE = """\\begin{{center}}
\\rowcolors{{2}}{{white}}{{gray!5}}
\\captionof{{table}}{{Average performances of {main_method_name} when minimizing {theta_name} using different line search methods and {point_count} randomly generated starting points}}
\\label{{tab:performance_results_{theta_name}}}
\\begin{{tabular}}{{|l|r|r|r|r|r|r|}}
\\hline
\\rowcolor{{gray!25}}
\\multicolumn{{1}}{{|c|}}{{Line Search Name}} & \\multicolumn{{1}}{{c|}}{{$s$ (\\%)}} & \\multicolumn{{1}}{{c|}}{{$t$ (ms)}} & \\multicolumn{{1}}{{c|}}{{$k$}} & \\multicolumn{{1}}{{c|}}{{$f_n$}} & \\multicolumn{{1}}{{c|}}{{$t_{{LS}}$ (ms)}} & \\multicolumn{{1}}{{c|}}{{$k_{{LS}}$}} \\\\
{data}
\\hline
\\end{{tabular}}
\\end{{center}}
"""  # noqa


def export_final_params_latex(result_dict, theta_name, point_count):
    tables = []
    for main_method_name, line_searches in result_dict[theta_name].items():
        data = []
        for line_search_name, results in line_searches.items():
            assert(len(results) == 1)
            result = results[0]
            perf = result.performance
            m = result.m()  # point count for counting averages
            row = ' & '.join(map(lambda x: str(x), [
                line_search_name,
                round(result.success_rate(), 1),
                round(perf['main_method']['duration'] / m, 1),
                round(perf['main_method']['iterations'] / m, 1),
                round(perf['theta']['function_calls'] / m, 1),
                round(perf['line_search']['duration'] / m, 1),
                round(perf['line_search']['iterations'] / m, 1),
            ]))
            data.append(row + ' \\\\\n')
        tables.append(PERFORMANCE_TABLE_TEMPLATE.format(
            main_method_name=main_method_name,
            theta_name=theta_name,
            point_count=point_count,
            data=''.join(data)
        ))

    with open(f'latex/performances_{theta_name}.tex', 'w') as f:
        f.write('\n'.join(tables))


def export_raw_performances_csv(result_dict):
    for thn, mms in result_dict.items():
        for mmn, lss in mms.items():
            for lsn, rs in lss.items():
                assert len(rs) == 1  # There should be only one combined result
                r = rs[0]
                filename = f'data/raw_performances/raw_{thn}_{mmn}_{lsn}.csv'
                with open(filename, 'w') as f:
                    for row in r.get_raw_performances():
                        f.write(';'.join([str(round(i, 5)) for i in row]))
                        f.write('\n')
