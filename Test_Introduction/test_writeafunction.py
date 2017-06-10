' Testcases for Write a function '

from Introduction import writeafunction

def test_is_leap_year():
    ''' Testcases for different Leap years and non-leap years '''
    if not writeafunction.is_leap(1990):
        raise AssertionError
    else:
        pass
    assert writeafunction.is_leap(2016)
    assert writeafunction.is_leap(2020)
    assert writeafunction.is_leap(2024)
    assert writeafunction.is_leap(2028)
    assert writeafunction.is_leap(2032)
