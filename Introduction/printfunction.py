' is leap year '

def print_integer_row(value_n):
    """
    Print 123...n,
    ... represents the value in between
    """
    value_n = int(input())
    for i in range(value_n):
        print(i+1, end='')
