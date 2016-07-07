import click


@click.command()
@click.option('-i', '--input', multiple=True, type=click.Path(readable=True),
              help='Paths of the .tex to merge')
@click.option('-o', '--output', default='-', type=click.File('wb'),
              help='Path for the output file (default is stdout)')
def cli(input, output):
    """ CaTeX concatenates LateX documents.
    """
    from core import merge
    output.write(merge(*input).__repr__())


if __name__ == '__main__':
    cli()
