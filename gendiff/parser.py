import json

import yaml


def parse(content, format_name):
    if format_name == '.json':
        return json.load(content)
    if format_name == '.yaml' or format_name == '.yml':
        return yaml.safe_load(content)
    raise Exception('Comparison is available only for json and yaml files')
