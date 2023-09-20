


from lib.greet import greet

def test_greet():
    result = greet("matteo")
    assert result == "Hello, matteo!"
