'''  Testcases for Loops '''

from Introduction import loops

def test_loops_output(capsys):
    loops.loops(5)
    out,err = capsys.readouterr()
    assert out == "0\n1\n4\n9\n16\n"

def test_myoutput(capsys): # or use "capfd" for fd-level
    print ("hello")
    sys.stderr.write("world\n")
    out, err = capsys.readouterr()
    assert out == "hello\n"
    assert err == "world\n"
    print ("next")
    out, err = capsys.readouterr()
    assert out == "next\n"

    #source https://docs.pytest.org/en/latest/capture.html#accessing-captured-output-from-a-test-function