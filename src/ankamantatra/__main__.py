import click
import json
from utils import get_category_questions, get_questions_from_json


@click.group()
def cli():
    pass


@cli.command()
def play():
    pass


@cli.command()
@click.option('--category', '-c')
@click.option('--show-answer', '-sa', is_flag=True)
@click.option('--show-category', '-sc', is_flag=True)
def list(category, show_answer, show_category):
    if category:
        try:
            questions = get_category_questions(category)
        except KeyError:
            click.echo(f'"{category}" is not a valid category')
    else:
        questions = get_questions_from_json()

    for type, question_list in questions.items():
        for question in question_list:
            if show_answer:
                click.echo(f'{question["question"]}')
                click.echo(f'--> {question["answer"]}\n')
            else:
                click.echo(f'{question["question"]}')


if __name__ == "__main__":
    cli()
