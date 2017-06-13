' Testcases for Lists '
from BasicDataTypes import lists

def test_lists_insert_1(capsys):
    '''
    Testcase for insert
    '''
    arr = []
    arr = lists.insert(arr, 5, 0)
    print(arr)
    out, err = capsys.readouterr()
    assert out == '[5]\n'

def test_lists_insert_2(capsys):
    '''
    Testcase for insert
    '''
    arr = []
    arr = lists.insert(arr, 5, 0)
    arr = lists.insert(arr, 10, 1)
    print(arr)
    out, err = capsys.readouterr()
    assert out == '[5, 10]\n'


def test_lists_insert_3(capsys):
    '''
    Testcase for insert
    '''
    arr = []
    arr = lists.insert(arr, 5, 0)
    arr = lists.insert(arr, 10, 1)
    arr = lists.insert(arr, 6, 0)
    print(arr)
    out, err = capsys.readouterr()
    assert out == '[6, 5, 10]\n'


def test_lists_remove(capsys):
    '''
    Testcase for remove
    '''
    arr = []
    arr = lists.insert(arr, 5, 0)
    arr = lists.insert(arr, 10, 1)
    arr = lists.insert(arr, 6, 0)
    arr = lists.remove(arr, 6)
    print(arr)
    out, err = capsys.readouterr()
    assert out == '[5, 10]\n'


def test_lists_append_1(capsys):
    '''
    Testcase for append
    '''
    arr = []
    arr = lists.insert(arr, 5, 0)
    arr = lists.insert(arr, 10, 1)
    arr = lists.insert(arr, 6, 0)
    arr = lists.remove(arr, 6)
    arr = lists.append(arr, 9)
    print(arr)
    out, err = capsys.readouterr()
    assert out == '[5, 10, 9]\n'


def test_lists_append_2(capsys):
    '''
    Testcase for append
    '''
    arr = []
    arr = lists.insert(arr, 5, 0)
    arr = lists.insert(arr, 10, 1)
    arr = lists.insert(arr, 6, 0)
    arr = lists.remove(arr, 6)
    arr = lists.append(arr, 9)
    arr = lists.append(arr, 1)

    print(arr)
    out, err = capsys.readouterr()
    assert out == '[5, 10, 9, 1]\n'

def test_lists_sort(capsys):
    '''
    Testcase for sort
    '''
    arr = []
    arr = lists.insert(arr, 5, 0)
    arr = lists.insert(arr, 10, 1)
    arr = lists.insert(arr, 6, 0)
    arr = lists.remove(arr, 6)
    arr = lists.append(arr, 9)
    arr = lists.append(arr, 1)
    arr = lists.sort(arr)
    print(arr)
    out, err = capsys.readouterr()
    assert out == '[1, 5, 9, 10]\n'

def test_lists_pop(capsys):
    '''
    Testcase for pop
    '''
    arr = []
    arr = lists.insert(arr, 5, 0)
    arr = lists.insert(arr, 10, 1)
    arr = lists.insert(arr, 6, 0)
    arr = lists.remove(arr, 6)
    arr = lists.append(arr, 9)
    arr = lists.append(arr, 1)
    arr = lists.sort(arr)
    arr = lists.pop(arr)
    arr = lists.reverse(arr)
    print(arr)
    out, err = capsys.readouterr()
    assert out == '[9, 5, 1]\n'