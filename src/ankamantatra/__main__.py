import click

@click.group()
def cli():
    pass

@cli.command()
def play():
    pass

@cli.command()
def list():
    pass

if __name__ == "__main__":
    cli()