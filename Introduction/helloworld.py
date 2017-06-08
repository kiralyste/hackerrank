def greetings(msg):
    return print(msg)

def test_msg():
    assert greetings("Hello World!") == "Hellor World !"

if __name__ == '__main__':
    greetings("Hello, World!")

