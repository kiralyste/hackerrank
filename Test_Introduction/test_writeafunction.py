' Testcases for Write a function '

from Introduction import writeafunction

def test_is_leap_year():
    ''' Testcases for different Leap years '''
    assert writeafunction.is_leap(2016)
    assert writeafunction.is_leap(2020)
    assert writeafunction.is_leap(2024)
    assert writeafunction.is_leap(2028)
    assert writeafunction.is_leap(2032)

def test_is_not_leap_year():
    """
     Testcases for different non-leap years
    """
    if writeafunction.is_leap(2019):
        raise AssertionError
    else:
        pass
    if writeafunction.is_leap(2021):
        raise AssertionError
    else:
        pass
    if writeafunction.is_leap(2022):
        raise AssertionError
    else:
        pass
    if writeafunction.is_leap(2023):
        raise AssertionError
    else:
        pass
