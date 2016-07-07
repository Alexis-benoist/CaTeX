import os


def test_import():
    print os.getcwd()
    from catex import LaTeX


def test_import_():
    import catex


def test_latex_simple():
    from catex import LaTeX
    f1 = LaTeX("data/latex1.tex")
    f1.merge(f1)
