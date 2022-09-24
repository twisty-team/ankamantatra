import json


def get_questions_from_json():
    pass


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
