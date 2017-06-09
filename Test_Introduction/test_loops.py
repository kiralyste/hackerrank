'''  Testcases for Loops '''

from Introduction import loops

def test_loops_output(capsys):
    loops.loops(5)
    out = capsys.readouterr()
    assert out == "0\n1\n4\n9\n16"

    #source https://docs.pytest.org/en/latest/capture.html#accessing-captured-output-from-a-test-function