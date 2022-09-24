import json
import os

path = os.path.dirname(__file__)

def get_categories():
    with open('data.json') as f:
        data = json.load(f)
        return list(data.keys())

def get_all_questions():
    with open('data.json') as f:
        data = json.load(f)
        return data

def get_questions_of(category: str) -> list:
    with open('data.json') as f:
        data = json.load(f)
        try:
            return data[category]
        except KeyError:
            raise KeyError(f'Category {category} not found')
