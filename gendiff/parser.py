import json
import yaml
import os


def load_json(content):
    return json.loads(content)


def load_yaml(content):
    return yaml.safe_load(content)


extensions = {
    '.json': load_json,
    '.yml': load_yaml,
    '.yaml': load_yaml,
}


def read_file(file_path):
    _, file_extension = os.path.splitext(file_path)
    if file_extension not in extensions.keys():
        raise Exception(f'File {file_path} has an invalid extension. '
                        f'Please select JSON-file or YAML-file')
    with open(file_path) as f:
        return file_extension, f.read()


def parse(file_extension, content):
    return extensions.get(file_extension)(content)
