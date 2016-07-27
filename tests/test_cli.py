
def test_cli_pdf(tmpdir):
    from catex.cli import _cli
    tmp_file = tmpdir.join("test.pdf")
    files = ["tests/data/latex1.tex", "tests/data/latex2.tex"]
    _cli(files, tmp_file.strpath)
    assert tmp_file.exists()
