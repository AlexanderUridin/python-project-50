from gendiff.formaters.formater_json import convert_to_json
from gendiff.formaters.formater_plain import plain
from gendiff.formaters.formater_stylish import stylish


def apply_formatter(diff_tree, formatter_name):
    if formatter_name == 'stylish':
        return stylish(diff_tree)
    if formatter_name == 'plain':
        return plain(diff_tree)
    if formatter_name == 'json':
        return convert_to_json(diff_tree)
    raise Exception('Invalid format, choose from stylish, plain, json')
