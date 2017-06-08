def ifelse(n):
    if ((n % 2) == 0) and (n >=2) and (n <=5):
        return "Not Weird"
    if ((n % 2) == 0) and (n >=6) and (n <=20):
        return "Weird"
    if ((n % 2) == 0) and (n >20):
        return "Not Weird"
    else:
        if ((n % 2) > 0):
            return "Weird"