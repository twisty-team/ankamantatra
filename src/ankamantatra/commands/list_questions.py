import click

from utils import *


@click.command(name='list', help='List all available questions to play with.')
@click.option('--category', '-c')
@click.option('--show-answer', '-sa', is_flag=True)
@click.option('--show-category', '-sc', is_flag=True)
@click.option('--category-only', is_flag=True)
def list_questions(category, show_answer, show_category, category_only):

    def display_question(question, category):
        click.echo(f'{question["question"]}')
        if show_answer:
            click.echo(f'--> {question["answer"]}\n')
        if show_category:
            click.echo(f'{category}')

    if category_only:
        categories = get_categories()
        for category in categories:
            click.echo(category)
        return

    if category:
        try:
            questions = get_questions_of(category)
        except KeyError:
            click.echo(f'"{category}" is not a valid category')
        for type, questions in questions.items():
            for question in questions:
                display_question(question, category)
    else:
        questions = get_all_questions()
        for category, type in questions.items():
            for type, questions in type.items():
                for question in questions:
                    display_question(question, category)
