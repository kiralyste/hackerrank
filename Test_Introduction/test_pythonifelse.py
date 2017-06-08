""" Testcases for Python If-Else """
from Introduction import pythonifelse


def test_odd():
    """ if n is odd, print 'Weired' """
    assert pythonifelse.ifelse(3) == "Weird"
    assert pythonifelse.ifelse(99) == "Weird"
    assert pythonifelse.ifelse(69) == "Weird"
    assert pythonifelse.ifelse(5) == "Weird"
    assert pythonifelse.ifelse(15) == "Weird"

def test_even_in_range_2_5():
    """ if n is even and in the inclusive range of 2 to 5 print 'Not Weired' """
    assert pythonifelse.ifelse(2) == "Not Weird"
    assert pythonifelse.ifelse(4) == "Not Weird"

def test_even_in_range_6_20():
    """ if n is even and in the inclusive range of 6 to 20 print 'Weired' """
    assert pythonifelse.ifelse(6) == "Weird"
    assert pythonifelse.ifelse(8) == "Weird"
    assert pythonifelse.ifelse(10) == "Weird"
    assert pythonifelse.ifelse(12) == "Weird"
    assert pythonifelse.ifelse(14) == "Weird"
    assert pythonifelse.ifelse(16) == "Weird"
    assert pythonifelse.ifelse(18) == "Weird"
    assert pythonifelse.ifelse(20) == "Weird"

def test_even_greater_20():
    """ if n is even and greater than 20 print 'Not Weired' """
    assert pythonifelse.ifelse(20) == "Weird"
    assert pythonifelse.ifelse(421) == "Weird"
    assert pythonifelse.ifelse(21) == "Weird"
    assert pythonifelse.ifelse(311) == "Weird"
    assert pythonifelse.ifelse(31) == "Weird"
