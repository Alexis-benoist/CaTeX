# -*- coding: utf-8 -*-


def test_import():
    from catex import LaTeX


def test_import_():
    import catex


def test_latex_simple():
    from catex import LaTeX
    f1 = LaTeX.from_file("tests/data/latex1.tex")
    f1.merge(f1)


def test_merge():
    from catex.core import merge
    rv = merge("tests/data/latex1.tex", "tests/data/latex2.tex")
    print rv


def test_merge_packeges():
    from catex.core import merge_packages
    pkg1 = [
        ['th', ['mou', 'moi', 'mumu=tutu']],
        ['blo', []],
        ['bli', ['tut']],
        ['bli', []],
        ['bleh', []],
        ['bla', []]]
    pkg2 = [
        ['th', ['mou', 'moi', 'mumu=tutu']],
        ['blo', []],
        ['bli', ['tut']],
        ['bli', []],
        ['bleh', []],
        ['bla', []]
    ]
    pkg_rv = [
        ['th', ['mumu=tutu', 'mou', 'moi']],
        ['blo', []],
        ['bli', ['tut']],
        ['bli', ['tut']], ['bleh', []],
        ['bla', []]
    ]
    assert merge_packages(pkg1, pkg2) == pkg_rv


def test_repr():
    from catex.core import LaTeX
    l = LaTeX.from_file("tests/data/latex1.tex")
    with open("tests/data/latex1.tex", 'r') as f:
        text = f.readlines()

    assert l.__repr__() == ''.join(text)

