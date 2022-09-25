import click

from ankamantatra.utils import *
from click_help_colors import HelpColorsCommand

@click.command(
    name='list', 
    help='List all available questions to play with.',
    cls=HelpColorsCommand,
    help_headers_color='yellow',
    help_options_color='green'
)
@click.option('--category', '-c', help="Filter by TEXT")
@click.option('--show-answer', '-sa', is_flag=True)
@click.option('--show-category', '-sc', is_flag=True)
@click.option('--category-only', is_flag=True, help="Show only the categories and hide questions")
def list_questions(category, show_answer, show_category, category_only):

    def display_question(question, category, type):
        try:
            click.echo(
                f'{question["question"]} ({type} in {question["options"]})')
        except:
            click.echo(f'{question["question"]} ({type})')
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
            click.echo(f'"{category}" is not a valid category.\n Type "ankamantatra list --category-only" to see all available categories.')
            return
        for type, questions in questions.items():
            for question in questions:
                display_question(question, category, type)
    else:
        questions = get_all_questions()
        for category, type in questions.items():
            for type, questions in type.items():
                for question in questions:
                    display_question(question, category, type)
