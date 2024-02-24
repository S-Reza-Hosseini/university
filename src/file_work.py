import json

def choose_file_name():

    path = 'data.json'

    return path

def save_lecture_in_json(file_name:str, information:dict):

    with open(file_name, 'w+') as fp:

            json.dump(information, fp)
            
            
def read_data_file(file_name:str):

    with open('data.json', 'r') as fp:

        data = json.load(fp)
        return data