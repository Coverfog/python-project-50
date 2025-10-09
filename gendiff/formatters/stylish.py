def stylish(data, depth=0):
    lines = []
    indents = '    ' * depth

    for key, value in data.items():
        if isinstance(value, dict) and 'status' in value.keys():

            match value['status']:
                case 'nested':
                    nested_diff = stylish(value['value'], depth + 1)
                    lines.append(
                        f'{indents}    {key}: {nested_diff}'
                    )
                case 'unchanged':
                    lines.append(
                        f"{indents}    {key}: "
                        f"{process_value(value['value'], depth)}"
                    )
                case 'added':
                    lines.append(
                        f"{indents}  + {key}: "
                        f"{process_value(value['value'], depth)}"
                    )
                case 'removed':
                    lines.append(
                        f"{indents}  - {key}: "
                        f"{process_value(value['value'], depth)}"
                    )
                case 'changed':
                    lines.append(
                        f"{indents}  - {key}: "
                        f"{process_value(value['old_value'], depth)}"
                    )
                    lines.append(
                        f"{indents}  + {key}: "
                        f"{process_value(value['new_value'], depth)}"
                    )
        elif isinstance(value, dict):
            nested_diff = stylish(value, depth + 1)
            lines.append(
                f'{indents}    {key}: {nested_diff}'
            )
        else:
            lines.append(
                f'{indents}    {key}: {process_value(value, depth)}'
            )

    return "{\n" + "\n".join(lines) + f"\n{indents}}}"


def process_value(v, depth):

    if isinstance(v, dict):
        return stylish(v, depth + 1)
    elif v is True:
        return 'true'
    elif v is False:
        return 'false'
    elif v is None:
        return 'null'

    return str(v)
