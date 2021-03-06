# CaTeX

`TLDR`: `CaTeX` `C`oncatenates L`aTeX` documents with attention for properly merging the preamble.

## Install

Run in the terminal:

    $ pip install catex

Done!

## Use

To concatenate `first_doc.tex` and `second_doc.tex`, just run:

    $ catex -i first_doc.tex -i second_doc.tex -o output.tex

If you want to directly compile it to PDF, simply:

    $ catex -i first_doc.tex -i second_doc.tex -o output.pdf

If no output file is selected then the output
will be displayed in std_out.

## Test

Run `$ py.test tests`.

## Contribute

You can use Github's issues to provide feedback and
report bugs.

This is the alpha version.

Tested pull requests are welcome.
