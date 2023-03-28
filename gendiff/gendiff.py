from gendiff.parser import read_file, parse
from gendiff.formatters.stylish import make_stylish
from gendiff.formatters.plain import make_plain
from gendiff.formatters.json_f import make_json

FORMATTERS_MAP = {
    'stylish': make_stylish,
    'plain': make_plain,
    'json': make_json
}


def stringify(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    return value


def create_diff_tree(data1, data2):
    keys = sorted(data1.keys() | data2.keys())
    diff = {}
    for key in keys:
        if key not in data1:
            diff[key] = {'value': stringify(data2[key]), 'category': 'added'}
        elif key not in data2:
            diff[key] = {'value': stringify(data1[key]), 'category': 'deleted'}
        elif data1[key] == data2[key]:
            diff[key] = {'value': stringify(data1[key]),
                         'category': 'unchanged'}
        elif (isinstance(data1.get(key), dict)
              and isinstance(data2.get(key), dict)):
            diff[key] = {'value': create_diff_tree(data1[key], data2[key]),
                         'category': 'nested'}
        else:
            diff[key] = {'value': (stringify(data1[key]),
                                   stringify(data2[key])),
                         'category': 'changed'}
    return diff


def generate_diff(fpath1, fpath2, output_format='stylish'):
    content1, extension1 = read_file(fpath1)
    content2, extension2 = read_file(fpath2)
    file1, file2 = parse(content1, extension1), parse(content2, extension2)
    diff = create_diff_tree(file1, file2)
    formatter = FORMATTERS_MAP.get(output_format, 'stylish')
    return formatter(diff)
