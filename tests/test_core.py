# -*- coding: utf-8 -*-
import os


def test_import():
    from catex import LaTeX


def test_import_():
    import catex


def test_latex_simple():
    from catex import LaTeX
    f1 = LaTeX("tests/data/latex1.tex")
    f1.merge(f1)
