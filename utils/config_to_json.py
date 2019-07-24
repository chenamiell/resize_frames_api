import json

CONFIGURATION_PATH = 'config.json'


def load_json_file_to_dict():
    with open(CONFIGURATION_PATH, 'r') as json_file:
        data = json.load(json_file)
    return data
