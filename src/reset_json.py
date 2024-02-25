import json


def reset_json_file(file_path):
    with open(file_path, 'w') as fp:
        json.dump('', fp)



