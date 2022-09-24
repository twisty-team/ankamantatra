import json
import os

current_path = os.path.dirname(__file__)
file_path = os.path.join(current_path, 'data.json')

def get_categories():
    with open(file_path) as f:
        data = json.load(f)
        return list(data.keys())

def get_all_questions():
    with open(file_path) as f:
        data = json.load(f)
        return data

def get_questions_of(category: str) -> list:
    with open(file_path) as f:
        data = json.load(f)
        try:
            return data[category]
        except KeyError:
            raise KeyError(f'Category {category} not found')
