import json


def open_json(file_path):
    return json.load(open(f'{file_path}'))


def normalize_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    return value


def generate_diff(file_path1, file_path2):
    file1 = open_json(file_path1)
    file2 = open_json(file_path2)

    keys1 = set(file1)
    keys2 = set(file2)
    all_keys = keys1 | keys2
    deleted = keys1 - keys2
    remaining = keys1 & keys2
    added = keys2 - keys1

    lines = ['{']

    for key in sorted(all_keys):
        if key in deleted:
            lines.append(f'- {key}: {normalize_value(file1.get(key))}')
        elif key in remaining:
            if file1.get(key) == file2.get(key):
                lines.append(f'  {key}: {normalize_value(file1.get(key))}')
            else:
                lines.append(f'- {key}: {normalize_value(file1.get(key))}')
                lines.append(f'+ {key}: {normalize_value(file2.get(key))}')
        elif key in added:
            lines.append(f'+ {key}: {normalize_value(file2.get(key))}')

    lines.append('}')
    return '\n'.join(lines)
