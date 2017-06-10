' is leap year '

def is_leap(year):
    ''' Read year, the year that needs to be checked '''
    # The year can be evenly divided by 4;
    if ((year % 400) == 0) or ((year % 4) == 0) and ((year % 100) != 0):
        return True
        # If the year can be evenly divided by 100, it is NOT a leap year, unless;
        # The year is also evenly divisible by 400. Then it is a leap year.
    return False
