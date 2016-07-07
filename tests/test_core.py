# -*- coding: utf-8 -*-
import os


def test_import():
    from catex import LaTeX


def test_import_():
    import catex


def test_latex_simple():
    from catex import LaTeX
    f1 = LaTeX.from_file("tests/data/latex1.tex")

    print f1.merge(f1)


def test_merge():
    from catex.core import merge
    merge("tests/data/latex1.tex", "tests/data/latex2.tex")
