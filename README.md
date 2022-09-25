# ankamantatra
*Techzara WCC2 final week*

A simple CLI quizz game made.
The user can play within a specific category or mix them all.
A game session consists of 4 questions, each of different type.
A the end of a session, the user is prompted whether he wants to play again or not.

![preview.gif]()

## Installation
Type in the terminal :
```sh
pip install ankamantatra
```
Or you can clone this repository and install it manually by following the steps below:
```sh
git clone https://github.com/twisty-team/ankamantatra.git
```
```sh
pip install poetry
```
```sh
# in the project root directory
poetry build && poetry install
```
And finally
```sh
poetry run python -m ankamanatra
```
## Usage
```
Usage: ankamantatra [OPTIONS] COMMAND [ARGS]...

  A simple quizz game CLI

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  list  List all available questions to play with.
  play  Use to play quiz game

```

## Features
- Play quizz
- List questions or categories


## TODO
- [x] List available questions
- [ ] List available categories
- [x] Play quizz
- [ ] Good error handling
- [x] Populate data.json
- [x] Utils functions
- [ ] Add "Ankamantatra/Malagasy" category
- [ ] Add automated testing
- [ ] Add comments
- [ ] Improve documentation
