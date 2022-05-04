import json


def get_configs():
    with open('./configs.json') as f:
        return json.load(f)
