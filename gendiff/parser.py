import json
import yaml


def format_parser(file_path):
    if file_path.endswith('.json'):
        json_file = json.load(open(file_path))
        return json_file
    elif file_path.endswith('.yml') or file_path.endswith('.yaml'):
        yaml_file = yaml.safe_load(open(file_path))
        return yaml_file
    raise Exception(f'File {file_path} has an invalid extension.'
                    f'Please select JSON-file or YAML-file')
