import json
import yaml
import os


def load_json(file_path):
    return json.load(open(file_path))


def load_yaml(file_path):
    return yaml.safe_load(open(file_path))


EXTENSIONS = {
    '.json': load_json,
    '.yml': load_yaml,
    '.yaml': load_yaml,
}


def parse(file_path):
    _, file_extension = os.path.splitext(file_path)
    if file_extension in EXTENSIONS.keys():
        return file_extension
    raise Exception(f'File {file_path} has an invalid extension. '
                    f'Please select JSON-file or YAML-file')


def load_file(file_path):
    return EXTENSIONS.get(parse(file_path))(file_path)
