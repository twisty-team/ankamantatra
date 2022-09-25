import json
import os

path = os.path.dirname(__file__)

def get_questions_from_json():
    f = open(os.path.join(path,'data.json'),'r')
    data = json.load(f)
    f.close()
    return data

def get_categories_from_json():
    f = open(os.path.join(path,'data.json'),'r')
    data = json.load(f)
    f.close()
    return data
    