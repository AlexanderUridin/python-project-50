import itertools


ADD = '  + '  # indent for ADDed elements
DEL = '  - '  # indent for DELeted elements
SP = '    '   # indent only from SPaces for unchanged elements


def to_str(value, level):
    if isinstance(value, dict):
        return stylish(value, level)
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return str(value)


def stylish(diff_dict, level=0):
    current_indent = SP * level
    lines = []

    for key, diff_info in diff_dict.items():
        value = diff_info if not isinstance(diff_info, dict) \
            else diff_info.get('value', diff_info)

        status = '' if not isinstance(diff_info, dict) \
            else diff_info.get('status')

        if status == 'added':
            lines.append(
                f'{current_indent}{ADD}{key}: {to_str(value, level + 1)}'
            )
        elif status == 'deleted':
            lines.append(
                f'{current_indent}{DEL}{key}: {to_str(value, level + 1)}'
            )
        elif status == 'updated':
            value1, value2 = value
            lines.append(
                f'{current_indent}{DEL}{key}: {to_str(value1, level + 1)}'
            )
            lines.append(
                f'{current_indent}{ADD}{key}: {to_str(value2, level + 1)}'
            )
        else:
            lines.append(
                f'{current_indent}{SP}{key}: {to_str(value, level + 1)}'
            )

    result = itertools.chain("{", lines, [current_indent + "}"])
    return '\n'.join(result)
