from gendiff.config.json_parser import json_read


def generate_diff(filepath1, filepath2):
    data1 = json_read(filepath1)
    data2 = json_read(filepath2)

    all_keys = sorted(set(data1.keys()).union(data2.keys()))

    lines = []

    for key in all_keys:
        value1 = data1.get(key)
        value2 = data2.get(key)

        if value1 == value2:
            lines.append(f"  {key}: {value1}")
        elif value1 is None:
            lines.append(f"+ {key}: {value2}")
        elif value2 is None:
            lines.append(f"- {key}: {value1}")
        elif value1 != value2:
                lines.append(f"- {key}: {value1}")
                lines.append(f"+ {key}: {value2}")

    return "{\n" + "\n".join(lines) + "\n}"
