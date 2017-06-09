'''  Testcases for Arithmetic Operators '''
from Introduction import arithmeticoperators

def test_sum():
    ''' add two values and return sum  '''
    assert arithmeticoperators.add(1, 2) == 3
    assert arithmeticoperators.add(2, 3) == 5
    assert arithmeticoperators.add(3, 2) == 5
    assert arithmeticoperators.add(354, 481) == 935
    assert arithmeticoperators.add(154, 3967) == 4121

def test_minus():
    ''' sub two values '''
    assert arithmeticoperators.minus(3, 2) == 1
    assert arithmeticoperators.minus(5, 2) == 3
    assert arithmeticoperators.minus(8, 3) == 5
    assert arithmeticoperators.minus(354, 20) == 334
    assert arithmeticoperators.minus(0, 3967) == -3967

def test_multiply():
    ''' multiply two values '''
    assert arithmeticoperators.mul(3, 2) == 6
    assert arithmeticoperators.mul(8, 3) == 24
    assert arithmeticoperators.mul(6, 6) == 36

