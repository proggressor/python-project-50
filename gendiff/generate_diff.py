import json
import itertools


def stringify(value):
    if isinstance(value, bool):
        return str(value).lower()
    return value


def diff_tree(data1, data2):
    keys = (data1.keys() | data2.keys())
    result = {}
    for key in keys:
        if key not in data1:
            result[key] = {'key': key, 'value': stringify(data2.get(key)),
                           'category': 'added'}
        elif key not in data2:
            result[key] = {'key': key, 'value': stringify(data1.get(key)),
                           'category': 'deleted'}
        elif data1[key] == data2[key]:
            result[key] = {'key': key, 'value': stringify(data1.get(key)),
                           'category': 'unchanged'}
        else:
            result[key] = {'key': key, 'old': stringify(data1.get(key)),
                           'new': stringify(data2.get(key)),
                           'category': 'changed'}
    return result


def generate_diff(file1, file2):
    data1 = json.load(open(file1))
    data2 = json.load(open(file2))

    difference = diff_tree(data1, data2)
    lines = []

    for key in sorted(difference.keys()):
        match difference.get(key).get('category'):
            case 'added':
                lines.append(f'  + {key}: {difference.get(key).get("value")}')
            case 'deleted':
                lines.append(f'  - {key}: {difference.get(key).get("value")}')
            case 'unchanged':
                lines.append(f'    {key}: {difference.get(key).get("value")}')
            case 'changed':
                lines.append(f'  - {key}: {difference.get(key).get("old")}')
                lines.append(f'  + {key}: {difference.get(key).get("new")}')
    result = itertools.chain("{", lines, "}")
    return '\n'.join(result)
