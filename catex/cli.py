import click


@click.command()
@click.option('-i', '--input', multiple=True, type=click.Path(readable=True))
@click.option('-o', '--output', default='-', type=click.Path(writable=True))
def cli(input, output):
    """ CaTeX concatenates LateX documents.
    """
    from core import merge
    output.write(merge(input))


if __name__ == '__main__':
    cli()
