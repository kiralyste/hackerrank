'''  Testcases for Loops '''

from Introduction import loops

def test_loops_output(capsys):
    '''  testcase for 5 lines '''
    loops.loop(5)
    out, err = capsys.readouterr()
    assert out == """0
                     1
                     4
                     9
                     16\n"""