all = ['generate_diff']

import os

from gendiff.difference import build_diff_tree
from gendiff.formaters import apply_formatter
from gendiff.parser import parse


def get_content(file_path):
    _, extension = os.path.splitext(file_path)

    with open(f'{file_path}') as input:
        return parse(input, extension)


def generate_diff(file_path1, file_path2, format='stylish'):
    '''Function compares two configuration files and returns a difference.

    Keyword argument:
    format -- formatter name for presentation of files differences.
              There are 3 available formats: stylish (default), plain, json.
    '''
    content1, content2 = map(get_content, (file_path1, file_path2))
    diff_tree = build_diff_tree(content1, content2)

    return apply_formatter(diff_tree, format)
