import click
from click_help_colors import HelpColorsGroup

from .utils import *
from .commands.list_questions import list_questions
from .commands.play_quizz import play


@click.group(
    cls=HelpColorsGroup,
    help_headers_color='yellow',
    help_options_color='green'
)
@click.version_option(
    version='0.7.0',
    prog_name='Ankamantatra'
)
def main():
    """A simple quizz game CLI"""
    pass


main.add_command(list_questions)
main.add_command(play)


if __name__ == "__main__":
    print("""
             _                               _        _             
            | |                             | |      | |            
  __ _ _ __ | | ____ _ _ __ ___   __ _ _ __ | |_ __ _| |_ _ __ __ _ 
 / _` | '_ \| |/ / _` | '_ ` _ \ / _` | '_ \| __/ _` | __| '__/ _` |
| (_| | | | |   < (_| | | | | | | (_| | | | | || (_| | |_| | | (_| |
 \__,_|_| |_|_|\_\__,_|_| |_| |_|\__,_|_| |_|\__\__,_|\__|_|  \__,_|     

    """)
    main()
