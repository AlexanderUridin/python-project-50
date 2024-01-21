import yaml


def convert_yaml(file_path1, file_path2):
    with open(f'{file_path1}') as input1:
        file1 = yaml.load(input1, Loader=yaml.FullLoader)
    with open(f'{file_path2}') as input2:
        file2 = yaml.load(input2, Loader=yaml.FullLoader)
    return file1, file2
