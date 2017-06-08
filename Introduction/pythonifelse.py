''' Python If-Else '''

def ifelse(num):
    ''' Handle different if-else Statements '''
    if ((num % 2) == 0) and (num >= 2) and (num <= 5):
        return "Not Weird"
    if ((num % 2) == 0) and (num >= 6) and (num <= 20):
        return "Weird"
    if ((num % 2) == 0) and (num > 20):
        return "Not Weird"
    else:
        if (num % 2) > 0:
            return "Weird"
            