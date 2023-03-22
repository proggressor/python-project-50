def plain_tail(value):
    str_exceptions = {'true', 'false', 'null'}
    if value == '':
        return "''"
    elif isinstance(value, dict) or isinstance(value, list):
        return '[complex value]'
    elif isinstance(value, str) and value not in str_exceptions:
        return f"'{value}'"
    return value


def plain_diff(diff, last_key=None):
    lines = []
    for key, data in diff.items():
        key_path = f'{last_key}.{key}' if last_key else key
        value, category = data.values()
        match category:
            case 'changed':
                old, new = [plain_tail(changed) for changed in value]
                lines.append(f'Property \'{key_path}\' was updated. '
                             f'From {old} to {new}')
            case 'nested':
                lines.extend(plain_diff(value, last_key=key_path))
            case 'added':
                value = plain_tail(value)
                lines.append(f'Property \'{key_path}\' was '
                             f'added with value: {value}')
            case 'deleted':
                lines.append(f'Property \'{key_path}\' was removed')
    return lines


def make_plain(diff):
    return '\n'.join(plain_diff(diff))  # , diff
