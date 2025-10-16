def plain(data, prefix=None):
    lines = []

    if prefix is None:
        prefix = []

    for key, value in data.items():

        match value['status']:
            case 'nested':
                prefix.append(str(key))
                lines.append(plain(value['value'], prefix))
                prefix.pop()
            case 'added':
                prefix.append(str(key))
                lines.append(
                    f"Property '{".".join(prefix)}' was added "
                    f'with value: {process_value(value['value'])}'
                )
                prefix.pop()
            case 'removed':
                prefix.append(str(key))
                lines.append(
                    f"Property '{".".join(prefix)}' was removed"
                )
                prefix.pop()
            case 'changed':
                prefix.append(str(key))
                lines.append(
                    f"Property '{".".join(prefix)}' was updated. "
                    f'From {process_value(value['old_value'])} '
                    f'to {process_value(value['new_value'])}'
                )
                prefix.pop()

    return '\n'.join(lines)


def process_value(v):

    if isinstance(v, dict):
        return '[complex value]'
    elif v is True:
        return 'true'
    elif v is False:
        return 'false'
    elif v is None:
        return 'null'
    elif isinstance(v, int):
        return str(v)

    return f"'{str(v)}'"
