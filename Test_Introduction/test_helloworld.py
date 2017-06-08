""" Testcases for Hello World! """
from Introduction import helloworld

def test_msg_1():
    """ function parameter 'Hello' should be also returned """
    assert helloworld.greetings("Hello") == "Hello"

def test_msg_2():
    """ function parameter 'Hello World!' should be also returned"""
    assert helloworld.greetings("Hello World!") == "Hello World!"
