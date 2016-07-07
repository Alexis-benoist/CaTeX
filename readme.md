
# CaTeX

`TLDR`: `CaTeX` `C`oncatenates L`ateX` documents.

## Install

Run in the terminal:

    $ pip install catex

Done!

## Use

To concatenate `first_doc.tex` and `second_doc.tex`, just run:

    $ catex -i first_doc.tex -i second_doc.tex -o output.tex

If no output file is selected then the output
will be displayed in std_out.

## Test

Run `$ py.test tests`.

## Contribute

You can use Github's issues to provide feedback and
report bugs.

Tested pull requests are welcome.