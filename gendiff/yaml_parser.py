import yaml


def convert_yaml(file_path1, file_path2):
    file1 = yaml.load(open(f'{file_path1}'), Loader=yaml.FullLoader)
    file2 = yaml.load(open(f'{file_path2}'), Loader=yaml.FullLoader)
    return file1, file2
