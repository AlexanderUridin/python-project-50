import json


def get_normal_value(file, key):
    value = file.get(key)
    if isinstance(value, bool):
        return str(value).lower()
    return value


def generate_diff(file_path1, file_path2):
    file1 = json.load(open(f'{file_path1}'))
    file2 = json.load(open(f'{file_path2}'))

    keys1 = set(file1)
    keys2 = set(file2)
    all_keys = keys1 | keys2
    deleted = keys1 - keys2
    remaining = keys1 & keys2
    added = keys2 - keys1

    lines = ['{']

    for key in sorted(all_keys):
        if key in deleted:
            lines.append(f'- {key}: {get_normal_value(file1, key)}')
        elif key in remaining:
            if file1.get(key) == file2.get(key):
                lines.append(f'  {key}: {get_normal_value(file1, key)}')
            else:
                lines.append(f'- {key}: {get_normal_value(file1, key)}')
                lines.append(f'+ {key}: {get_normal_value(file2, key)}')
        elif key in added:
            lines.append(f'+ {key}: {get_normal_value(file2, key)}')

    lines.append('}')
    return '\n'.join(lines)
