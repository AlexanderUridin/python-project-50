from gendiff.yaml_parser import convert_yaml
from gendiff.json_parser import convert_json
from gendiff.parsing import parse


def generate_diff(file_path1, file_path2):
    if file_path1.endswith('json') and file_path2.endswith('json'):
        file1, file2 = convert_json(file_path1, file_path2)
    else:
        file1, file2 = convert_yaml(file_path1, file_path2)

    lines = parse(file1, file2)

    lines.insert(0, '{')
    lines.append('}')
    return '\n'.join(lines)
