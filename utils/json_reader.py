import json


def get_json_data(file_path):

    with open(file_path) as json_file:

        data = json.load(json_file)

    return [
        item["product"]
        for item in data
    ]