import json
import os

path = os.path.dirname(__file__)

def get_questions_from_json():
    f = open(os.path.join(path,'data.json'),'r')
    data = json.load(f)
    f.close()
    return data


def get_categories_from_json():
    with open('data.json') as f:
        data = json.load(f)
        return list(data.keys())


def get_category_questions(category: str) -> list:
    with open('data.json') as f:
        data = json.load(f)
        try:
            return data[category]
        except KeyError:
            raise KeyError(f'Category {category} not found')
