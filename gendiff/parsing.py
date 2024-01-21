def walk_unchanged(nest):
    if not isinstance(nest, dict):
        return nest
    nested_level = {}

    for key in sorted(set(nest)):
        nested_level[key] = {
            'value': walk_unchanged(nest.get(key))
        }
    return nested_level


def check_type(item1, item2):
    if not isinstance(item1, dict) and not isinstance(item2, dict):
        return [item1, item2]
    elif not isinstance(item1, dict) and isinstance(item2, dict):
        return [item1, walk_unchanged(item2)]
    elif isinstance(item1, dict) and not isinstance(item2, dict):
        return [walk_unchanged(item1), item2]
    else:
        return item1, item2


def walk(nest1, nest2):
    difference = {}

    keys1 = set(nest1)
    keys2 = set(nest2)

    all_keys = keys1 | keys2
    added = keys2 - keys1
    deleted = keys1 - keys2

    for key in sorted(all_keys):
        if key in added:
            difference[key] = {
                'status': 'added',
                'value': walk_unchanged(nest2.get(key))
            }
        elif key in deleted:
            difference[key] = {
                'status': 'deleted',
                'value': walk_unchanged(nest1.get(key))
            }
        elif nest1.get(key) == nest2.get(key):
            difference[key] = {
                'value': walk_unchanged(nest1.get(key))
            }
        elif isinstance(check_type(nest1.get(key), nest2.get(key)), tuple):
            dict1, dict2 = check_type(nest1.get(key), nest2.get(key))
            difference[key] = {
                'value': walk(dict1, dict2)
            }
        else:
            difference[key] = {
                'status': 'updated',
                'value': check_type(nest1.get(key), nest2.get(key))
            }
    return difference


def parse(file1, file2):
    return walk(file1, file2)
