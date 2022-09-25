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
            click.echo(f'{question["question"]} ', nl=False)
            click.echo(click.style(f'({type} in {question["options"]})', fg='blue'))
        except:
            click.echo(f'{question["question"]} ' + click.style(f'({type})', fg='blue'))
        if show_answer:
            click.echo(click.style(f'--> {question["answer"]}\n', fg='green'))
        if show_category:
            click.echo(click.style(f'[{category}]\n', fg='yellow'))

    if category_only:
        click.echo(click.style('Available categories:\n', fg='yellow'))
        categories = get_categories()
        for category in categories:
            click.echo(f'- {category}')
        return

    if category:
        click.echo(click.style(f'Questions about {category}\n', fg='yellow'))
        try:
            questions = get_questions_of(category)
        except KeyError:
            click.echo(click.style(f'"{category}" is not a valid category.\n', fg='red') + 'Type "ankamantatra list --category-only" to see all available categories.')
            return
        for type, questions in questions.items():
            for question in questions:
                display_question(question, category, type)
    else:
        questions = get_all_questions()
        click.echo(click.style('Question ', fg='yellow'), nl=False)
        click.echo(click.style('(type and optional choices)\n', fg='blue'))
        
        for category, type in questions.items():
            for type, questions in type.items():
                for question in questions:
                    display_question(question, category, type)
