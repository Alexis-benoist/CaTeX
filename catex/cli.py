import click


@click.command()
@click.option('-i', '--input', multiple=True, type=click.Path(readable=True),
              help='Paths of the .tex to merge')
@click.option('-i', '--input', multiple=True, type=click.Path(readable=True),
              help='Paths of the .tex to merge')
@click.option('-o', '--output', default='-', type=click.Path(readable=True),
              help='Path for the output file (default is stdout)')
def cli(input, output):
    """ CaTeX concatenates LateX documents.
    """
    _cli(input, output)


def _cli(input, output):
    from catex.core import merge
    text = merge(*input).__repr__()
    if output[-4:] == '.pdf':
        from latex import build_pdf
        pdf = build_pdf(text)
        pdf.save_to(output)
    else:
        file_out = click.open_file(output)
        file_out.write(text)

if __name__ == '__main__':
    cli()
