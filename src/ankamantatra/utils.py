import json
import os

path = os.path.dirname(__file__)

def get_questions_from_data(categorie):
    data = get_categories_from_json()
    return data[categorie]


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
