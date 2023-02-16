import itertools
from gendiff.parser import format_parser


def stringify(value):
    if isinstance(value, bool):
        return str(value).lower()
    return value


def diff_tree(data1, data2):
    keys = (data1.keys() | data2.keys())
    result = {}
    for key in keys:
        if key not in data1:
            result[key] = {'value': stringify(data2.get(key)),
                           'category': 'added'}
        elif key not in data2:
            result[key] = {'value': stringify(data1.get(key)),
                           'category': 'deleted'}
        elif data1[key] == data2[key]:
            result[key] = {'value': stringify(data1.get(key)),
                           'category': 'unchanged'}
        else:
            result[key] = {'old': stringify(data1.get(key)),
                           'new': stringify(data2.get(key)),
                           'category': 'changed'}
    return result


def generate_diff(f_path1, f_path2):
    difference = diff_tree(format_parser(f_path1), format_parser(f_path2))
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
