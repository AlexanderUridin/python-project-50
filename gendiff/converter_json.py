import json


def convert_json(file_path1, file_path2):
    with open(f'{file_path1}') as input1:
        file1 = json.load(input1)
    with open(f'{file_path2}') as input2:
        file2 = json.load(input2)
    return file1, file2
