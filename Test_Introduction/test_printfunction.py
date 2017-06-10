' Testcases for Print function '

from Introduction import printfunction

def test_printfunction(capsys):
    """
    Testcase for different small numbers
    """
    printfunction.print_integer_row(3)
    out, err = capsys.readouterr()
    assert out == "123"
       
    printfunction.print_integer_row(5)
    out, err = capsys.readouterr()
    assert out == "12345"

    printfunction.print_integer_row(10)
    out, err = capsys.readouterr()
    assert out == "12345678910"

    printfunction.print_integer_row(20)
    out, err = capsys.readouterr()
    assert out == "1234567891011121314151617181920"

    printfunction.print_integer_row(8)
    out, err = capsys.readouterr()
    assert out == "12345678"

    printfunction.print_integer_row(4)
    out, err = capsys.readouterr()
    assert out == "1234"
