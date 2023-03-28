import json
import yaml
import os


EXTENSIONS = {
    '.json': None,
    '.yml': None,
    '.yaml': None,
}


def load_json(content):
    return json.loads(content)


EXTENSIONS['.json'] = load_json


def load_yaml(content):
    return yaml.safe_load(content)


EXTENSIONS['.yml'] = load_yaml
EXTENSIONS['.yaml'] = load_yaml


def read_file(file_path):
    _, file_extension = os.path.splitext(file_path)
    if file_extension not in EXTENSIONS.keys():
        raise Exception(f'File {file_path} has an invalid extension. '
                        f'Please select JSON-file or YAML-file')
    with open(file_path) as f:
        return file_extension, f.read()


def parse(file_extension, content):
    return EXTENSIONS.get(file_extension)(content)
