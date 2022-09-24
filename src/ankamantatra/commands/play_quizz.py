import click
import random

from utils import *


def do_quiz(categorie):
    click.echo(click.style('Quiz categorie : ' + categorie, fg='blue'))
    data = get_questions_of(categorie)
    index = 1
    number_of_good_response = 0
    for type, questions in data.items():
        for item in questions:
            questions = item['question']
            click.echo(click.style(
                f'Question {index} : type = {type}', fg="blue"))
            key = random.randrange(0, len(questions))
            click.echo(click.style(item['question'], fg="blue"))

            if type == "multiple":
                opt = "| "
                for val in item['options']:
                    opt += f"{val}  |  "
                click.echo(f"Options : {opt}")
                click.echo(click.style(
                    "your reponse should be separated by space", fg="yellow"))
                reponses = click.prompt("your answer > ")
                rep_arr = reponses.split(' ')
                print(rep_arr)
                count = 0
                for ans in rep_arr:
                    if ans in item['answer']:
                        count += 1
                if count == len(item['answer']):
                    number_of_good_response += 1

            elif type == "unique":
                opt = "| "
                for val in item['options']:
                    opt += f"{val}  |  "
                click.echo(f"Options : {opt}")
                reponse = click.prompt("your answer > ")
                if reponse in item['answer']:
                    number_of_good_response += 1

            elif type == "number":
                reponse = click.prompt("your answer > ", type=int)
                if reponse == item['answer']:
                    number_of_good_response += 1

            elif type == "string":
                reponse = click.prompt("your answer > ", type=str)
                if reponse == item['answer']:
                    number_of_good_response += 1

        index += 1
    click.echo(f"Total of good answer {number_of_good_response}")


@click.command()
@click.option('categorie', '--categorie', help="Help for Play command")
def play(categorie):
    categories = get_categories()
    index = 1
    while categorie not in categories:
        fg = 'green'
        if index > 1:
            fg = 'red'
        click.echo(click.style("Please choose categorie : ", fg=fg))
        val = "| "
        for cat in categories:
            val += f" {cat}  |  "
        click.echo(val)
        categorie = click.prompt("Categorie > ", type=str)
        index += 1
    do_quiz(categorie)
