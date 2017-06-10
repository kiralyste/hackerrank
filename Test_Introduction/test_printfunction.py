' Testcases for Print function '

from Introduction import printfunction

def test_printfunction():
    """
    Testcase for different small numbers
    """
    assert printfunction.print_integer_row(3) == 123
    assert printfunction.print_integer_row(5) == 12345
    assert printfunction.print_integer_row(10) == 12345678910
    assert printfunction.print_integer_row(20) == 1234567891011121314151617181920
    assert printfunction.print_integer_row(8) == 12345678
    assert printfunction.print_integer_row(4) == 1234
    