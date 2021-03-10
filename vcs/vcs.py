import click

@click.group()
def cli():
    pass


@click.command()
def init():
    print("Init repo")


@click.command()
def commit():
    print("commit")


if __name__ == '__main__':
    cli.add_command(init)
    cli.add_command(commit)
    cli()