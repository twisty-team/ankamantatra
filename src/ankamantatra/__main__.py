import click
from click_help_colors import HelpColorsGroup, HelpColorsCommand

from utils import *
from commands.list_questions import list_questions
from commands.play_quizz import play


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


cli.add_command(list_questions)
cli.add_command(play)


if __name__ == "__main__":
    cli()
