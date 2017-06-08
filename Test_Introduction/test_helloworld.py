from Introduction import helloworld

def test_msg_1():
    assert helloworld.greetings("Hello") == "Hello"

def test_msg_2():
    assert helloworld.greetings("Hello World") == "Hello World!"
