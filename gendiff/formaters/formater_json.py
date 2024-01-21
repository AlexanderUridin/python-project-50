import json


def convert_to_json(diff_tree):
    return json.dumps(diff_tree, indent=4)
