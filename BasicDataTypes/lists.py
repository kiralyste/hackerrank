"""
Problem: implement follow commands
 1) insert i e: Insert integer e at position i
 2) print: Print the list
 3) remove e: Delete the first occurrence of integer e
 4) append e: Insert integer e at the end of the list
 5) sort: Sort the list
 6) pop: Pop the last element from the list
 7) Reverse: Reverse the list
"""

def insert(arr, value=0, pos=0):
    '''
    Insert integer e at position i
    '''
    arr.insert(int(pos), int(value))
    return arr

def remove(arr, value):
    '''
    Delete the first occurrence of integer e
    '''
    arr.remove(int(value))
    return arr

def append(arr, value):
    '''
    Insert integer e at the end of the list.
    '''
    arr.append(int(value))
    return arr

def sort(arr):
    '''
    Sort the list.
    '''
    arr.sort()
    return arr

def pop(arr):
    '''
    Pop the last element fromt the list.
    '''
    arr.pop()
    return arr

def reverse(arr):
    '''
    Reverse the list.
    '''
    arr.reverse()
    return arr

def start():
    N = int(input())

    arr = []
    command = ''

    for i in range(N):
        #read commandline
        line = input()
        #split commands and get first command
        command = line.split()[0]
        #check which command it es
        if command == 'insert':
            pos = line.split()[1]
            val = line.split()[2]
            arr = insert(arr, val, pos)
        elif command == "print":
            print(arr)
        elif command == "remove":
            val = line.split()[1]
            arr = remove(arr, int(val))
        elif command == "append":
            val = line.split()[1]
            arr = append(arr, int(val))
        elif command == "sort":
            arr = sort(arr)
        elif command == "pop":
            arr = pop(arr)
        elif command == "reverse":
            arr = reverse(arr)
        else:
            print("command unknown")
            