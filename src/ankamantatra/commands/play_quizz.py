from operator import is_
from unittest import result
import click
import random
from click_help_colors import HelpColorsCommand

from ankamantatra.utils import *


def quiz_operation(type, questions, result):
    type = type
    questions = questions
    result = result
    random_key = random.randrange(0, len(questions))
    question = questions[random_key]
    click.echo(click.style(f"> {question['question']}"))
    if type == "multiple":
        opt = ""
        i = 1
        for val in question['options']:
            opt += click.style(f"({i})", fg="yellow") + f" {val}  "
            i += 1
        click.echo(f"> Options : {opt}")
        click.echo(click.style(
            "N.B : your reponse should be separated by space, for example: 1 3 5", fg="yellow")
        )
        # On verfie si les input de l'utilisateur sont parmis les listes
        is_valid = False
        rep_arr = []
        while is_valid == False:
            reponses = click.prompt("your answer ", type=str)
            rep_arr = reponses.split(' ')
            for rep in rep_arr:
                ind = None
                try:
                    ind = int(rep) - 1
                except:
                    is_valid = False
                    click.echo(
                        click.style(
                        "The expected response is a sequence of number and should be among the options given , Please Retry",
                        fg='red'
                        )
                    )
                    break

                if  ind >= len(question['options']) or ind < 0:
                    is_valid = False
                    click.echo(
                        click.style(
                        "The expected response is a sequence of number and should be among the options given , Please Retry",
                        fg='red'
                        )
                    )
                    break
                else:
                    is_valid = True
        count = 0
        for ind in rep_arr:
            if question["options"][int(ind) - 1] in question['answer']:
                count += 1
            
        if count == len(question['answer']):
            result['Q1'] = True
        else:
            result['Q1'] = False

    elif type == "unique":
        opt = ""
        i = 1
        for val in question['options']:
            opt += click.style(f"({i})", fg="yellow") + f" {val} "
            i += 1
        click.echo(f"> Options : {opt}")
        
        #on verifie si l'entree est valide
        is_valid = False
        rep_arr = []
        while not is_valid:
            reponse_index = click.prompt("your answer ")
            rep_arr = reponse_index.split(" ")
            if len(rep_arr) == 1:
                is_parsable_to_int = False
                try:
                    int(rep_arr[0])
                    is_parsable_to_int = True
                except:
                    is_valid = False
                    click.echo(
                        click.style(
                            "The expected response is of type number, Please Retry",
                            fg='red'
                        )
                    )
                if is_parsable_to_int:
                    if int(rep_arr[0]) >= len(question['options']) or int(rep_arr[0]) <= 0:
                        is_valid = False
                        click.echo(
                            click.style(
                                "The expected response should be among the options given, Please Retry",
                                fg='red'
                            )
                        )
                    else:
                        is_valid = True
            else:
                is_valid = False
                click.echo(
                    click.style(
                        "The expected response is unique, Please Retry",
                        fg='red'
                    )
                )
        if question["options"][int(rep_arr[0]) - 1] == question['answer']:
            result['Q2'] = True
        else:
            result['Q2'] = False

    elif type == "number":
        reponse = click.prompt("your answer ", type=int)
        if reponse == question['answer']:
            result['Q3'] = True
        else:
            result['Q3'] = False

    elif type == "string":
        reponse = click.prompt("your answer ", type=str)
        if reponse.lower() == question['answer'].lower():
            result['Q4'] = True
        else:
            result['Q4'] = False
            
    return result


def do_quiz(categorie):
    number_of_good_answer = 0
    result = {}
    click.echo('')
    click.echo(click.style('___Quiz category___ : ' + categorie, fg='blue'))
    click.echo('')
    if categorie == 'all':
        categories = get_categories()
        all_types = ['multiple', 'unique', 'number', 'string']
        index = 1
        for t in all_types:
            random_key = random.randrange(0, len(categories))
            cat = categories[random_key]
            data = get_questions_of(cat)
            click.echo(click.style(
                f'___Question {index}___ : type = {t}', fg="blue")
            )
            for type, questions in data.items():
                if type == t:
                    result_of_game = quiz_operation(t, questions, result)
            index += 1

    else:
        data = get_questions_of(categorie)
        index = 1
        for type, questions in data.items():
            click.echo(click.style(
                f'___Question {index}___ : type = {type}', fg="blue")
            )
            result_of_game = quiz_operation(type ,questions, result)
            index += 1

    number_of_good_answer = 0
    for q, r in result_of_game.items():
        if r == True:
            number_of_good_answer += 1
            
    click.echo('')
    click.echo(click.style('__RESULTATS__', fg='green'))
    click.echo(f"Total of good answer {number_of_good_answer}", nl=True)
    v = 0
    f = 0
    for q, res in result.items():
        if res:
            v += 1
        else:
            f += 1
        click.echo(f"{q} : {res}")
    success_rate = (v / (v + f)) * 100
    color = ''
    if success_rate >= 75:
        color = 'green'
    elif success_rate >= 25:
        color = 'yellow'
    else:
        color = 'red'
    click.echo(click.style(f"Success rate : {success_rate} %", fg=color))


@click.command(
    name="play",
    help="Use to play quiz game",
    cls=HelpColorsCommand,
    help_headers_color='yellow',
    help_options_color='green'
)
@click.option('category', '--category', '-c', help="Specify Quiz categorie")
def play(category):
    click.clear()
    click.echo(click.style('___QUIZ APP___', fg="green", bold=True))
    categories = get_categories()
    index = 1
    if category is None:
        choice = click.confirm(
            'Category is not specified! Do you want to choose a category? ' + click.style('[default = No]', bg="blue"),
            default=False)
        if choice:
            while category not in categories:
                fg = 'green'
                if index > 1:
                    fg = 'red'
                click.echo(click.style("Please choose category : ", fg=fg))
                val = ""
                i = 1
                for cat in categories:
                    val += click.style(f"({i})", fg='yellow') + f" {cat}  "
                    i += 1
                click.echo(val)
                indice_categorie = click.prompt("Category", type=int)
                indice_categorie -= 1
                if indice_categorie < len(categories) and indice_categorie >= 0:
                    category = categories[indice_categorie]
                index += 1
        else:
            category = "all"
    else:
        if category not in categories:
            click.echo('')
            click.echo(click.style("this category is not specified! default: Category = all", fg='yellow'))
            category = 'all'
    do_quiz(category)
