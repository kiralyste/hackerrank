'''  Testcases for Loops '''

from Introduction import loops

def test_loops_output(capsys):
    '''  testcase for 5 lines '''
    loops.loop(5)
    out, err = capsys.readouterr()
    cmdout_line = "0\n" + "1\n" + "4\n" + "9\n" + "16\n"
    assert out == cmdout_line
