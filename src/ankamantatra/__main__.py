import click
import random
from click_help_colors import HelpColorsGroup, HelpColorsCommand
import ecdsa

from utils import get_categories_from_json, get_questions_from_data

def do_quiz(categorie):
    click.echo(click.style('Quiz categorie : ' + categorie, fg='blue'))
    data = get_questions_from_data(categorie)
    index = 1
    number_of_good_response = 0
    for types in data:
        for item in types.items():
            tp = item[0]
            questions = item[1]
            click.echo(click.style(f'Question {index} : type = {tp}', fg="blue"))
            key = random.randrange(0, len(questions))
            click.echo(click.style(questions[key]['question'], fg="blue"))
            
            if tp == "multiple":
                opt = "| "
                for val in questions[key]['options']:
                    opt += f"{val}  |  "
                click.echo(f"Options : {opt}")
                click.echo(click.style("your reponse should be separated by space", fg="yellow"))
                reponses = click.prompt("your answer > ")
                rep_arr = reponses.split(' ')
                print(rep_arr)
                count = 0
                for ans in rep_arr:
                    if ans in questions[key]['answer']:
                        count += 1
                if count == len(questions[key]['answer']):
                    number_of_good_response += 1
                     
            elif tp == "unique":
                opt = "| "
                for val in questions[key]['options']:
                    opt += f"{val}  |  "
                click.echo(f"Options : {opt}")
                reponse = click.prompt("your answer > ")
                if reponse in questions[key]['answer']:
                    number_of_good_response += 1
                    
            elif tp == "number":
                reponse = click.prompt("your answer > ", type=int)
                if reponse == questions[key]['answer']:
                    number_of_good_response += 1
                    
            elif tp == "string":
                reponse = click.prompt("your answer > ", type=str)
                if reponse == questions[key]['answer']:
                    number_of_good_response += 1
           
        index +=1
    click.echo(f"Total of good answer {number_of_good_response}")


@click.group(
    cls=HelpColorsGroup,
    help_headers_color='yellow',
    help_options_color='green'
)
@click.version_option(
    version='1.0',
    prog_name='Ankamantatra'
)
def cli():
    pass


@cli.command()
@click.option('categorie', '--categorie', help="Help for Play command")
def play(categorie):
    categories = get_categories_from_json()
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
