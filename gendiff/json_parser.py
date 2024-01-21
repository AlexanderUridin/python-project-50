import json


def convert_json(file_path1, file_path2):
    file1 = json.load(open(f'{file_path1}'))
    file2 = json.load(open(f'{file_path2}'))
    return file1, file2
