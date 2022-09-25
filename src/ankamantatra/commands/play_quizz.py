import click
import random
from click_help_colors import HelpColorsCommand

from ankamantatra.utils import *

def do_quiz(categorie):
    click.echo('')
    click.echo(click.style('___Quiz categorie___ : ' + categorie , fg='blue'))
    data = get_questions_of(categorie)
    index = 1
    number_of_good_response = 0
    result = {}
    for type, questions in data.items():
        click.echo('')
        click.echo(click.style(
            f'___Question {index}___ : type = {type}', fg="blue")
        )
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
            reponses = click.prompt("your answer ", type=str)
            rep_arr = reponses.split(' ')
            count = 0
            for ind in rep_arr:
                try:
                    if question["options"][int(ind) - 1] in question['answer']:
                        count += 1
                except:
                    result['Q1'] = False
                    click.echo(click.style("The expected response is a sequence of number, your answer is considered wrong", fg='red'))
            if count == len(question['answer']):
                result['Q1'] = True
                number_of_good_response += 1
            else:
                result['Q1'] = False

        elif type == "unique":
            opt = ""
            i = 1
            for val in question['options']:
                opt += click.style(f"({i})", fg="yellow") + f" {val} "
                i += 1
            click.echo(f"> Options : {opt}")
            reponse_index = click.prompt("your answer ")
            try:
                if question["options"][int(reponse_index) - 1] in question['answer']:
                    number_of_good_response += 1
                    result['Q2'] = True
                else:
                    result['Q2'] = False
            except:
                result['Q2'] = False
                click.echo(click.style("The expected response is of type number, your answer is considered wrong", fg='red'))

        elif type == "number":
            reponse = click.prompt("your answer ", type=str)
            try:
                if int(reponse) == question['answer']:
                    number_of_good_response += 1
                    result['Q3'] = True
                else:
                    result['Q3'] = False
            except:
                result['Q3'] = False
                click.echo(click.style("The expected response is of type number, your answer is considered wrong", fg='red'))
            
        elif type == "string":
            reponse = click.prompt("your answer ", type=str)
            if reponse.lower() == question['answer'].lower():
                number_of_good_response += 1
                result['Q4'] = True
            else:
                result['Q4'] = False

        index += 1
        
    click.echo('')
    click.echo(click.style('__RESULTATS__', fg='green'))
    click.echo(f"Total of good answer {number_of_good_response}", nl=True)
    v = 0
    f = 0
    for q, res in result.items():
        if res:
            v += 1
        else:
            f +=1
        click.echo(f"{q} : {res}")
    success_rate = (v / (v+f))*100
    click.echo(click.style(f"Success rate : {success_rate} %", fg="green"))


@click.command(
    name="play", 
    help="Use to play quiz game",
    cls=HelpColorsCommand,
    help_headers_color='yellow',
    help_options_color='green'
)
@click.option('categorie', '--categorie', help="Specify Quiz categorie")
def play(categorie):
    click.echo(click.style('___QUIZ APP___', fg="green", bold=True))
    categories = get_categories()
    index = 1
    while categorie not in categories:
        fg = 'green'
        if index > 1:
            fg = 'red'
        click.echo(click.style("Please choose categorie : ", fg=fg))
        val = ""
        i = 1
        for cat in categories:
            val += click.style(f"({i})", fg='yellow') + f" {cat}  "
            i += 1
        click.echo(val)
        indice_categorie = click.prompt("Categorie ", type=int)
        indice_categorie -= 1
        if indice_categorie < len(categories) and indice_categorie >= 0:
            categorie = categories[indice_categorie]
        index += 1
    do_quiz(categorie)
