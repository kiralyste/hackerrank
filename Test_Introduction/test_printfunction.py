' Testcases for Print function '

from Introduction import printfunction

def test_printfunction():
    """
    Testcase for different small numbers
    """
    printfunction.print_integer_row(3)
    out, err = capsys.readouterr()
    assert out == 123    