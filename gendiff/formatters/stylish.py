import itertools

DEFAULT_INDENT = 4
categories_map = {'added': '+', 'deleted': '-'}


def make_stylish(diff, spaces=0, replacer=' '):
    if not isinstance(diff, dict):
        return str(diff)
    indent = replacer * (spaces + 2)
    last_indent = replacer * spaces + '}'
    spaces += DEFAULT_INDENT
    lines = []
    for key, data in diff.items():
        if isinstance(data, dict):
            category = data.get('category', 'unchanged')
            value = data.get('value', data)
        else:
            category, value = 'unchanged', data
        match category:
            case 'changed':
                old, new = [make_stylish(changed, spaces) for changed in value]
                lines.append(f'{indent}- {key}:{" " if old else ""}{old}')
                lines.append(f'{indent}+ {key}:{" " if new else ""}{new}')
            case 'nested':
                value = make_stylish(value, spaces)
                lines.append(f'{indent}  {key}: {value}')
            case _:
                cat = categories_map.get(category, replacer)
                lines.append(f'{indent}{cat} {key}: '
                             f'{make_stylish(value, spaces)}')
    result = itertools.chain("{", lines, [last_indent])
    return '\n'.join(result)
