import itertools


ADD = '  + '  # indent for ADDed elements
DEL = '  - '  # indent for DELeted elements
SP = '    '   # indent only from SPaces for unchanged elements


def get_normal_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    return str(value)


def walk(diff_dict, level):
    if not isinstance(diff_dict, dict):
        return get_normal_value(diff_dict)

    current_indent = SP * level
    lines = []

    for key, diff_info in diff_dict.items():
        value = diff_info['value']
        status = diff_info['status']

        if status == 'added':
            lines.append(
                f'{current_indent}{ADD}{key}: {walk(value, level + 1)}'
            )
        elif status == 'deleted':
            lines.append(
                f'{current_indent}{DEL}{key}: {walk(value, level + 1)}'
            )
        elif status == 'remaining' or status == 'changed':
            lines.append(
                f'{current_indent}{SP}{key}: {walk(value, level + 1)}'
            )
        else:
            value1, value2 = value
            lines.append(
                f'{current_indent}{DEL}{key}: {walk(value1, level + 1)}'
            )
            lines.append(
                f'{current_indent}{ADD}{key}: {walk(value2, level + 1)}'
            )

    result = itertools.chain("{", lines, [current_indent + "}"])
    return '\n'.join(result)


def stylish(difference_dictionary):
    return walk(difference_dictionary, 0)
