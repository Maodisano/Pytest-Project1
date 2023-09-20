

import pytest
from lib.present import *

#when wrapping an item - we get it back when unwrapped

def test_wrap_and_then_unwrap():
    present = Present()
    present.wrap(33)
    assert present.unwrap() == 33

#test is we unwrap before wrapping - exception raised

def test_unwrap_without_wrapping():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."

# if we try to wrap and already wrapped present we get an error message

def test_wrap_already_wrapped():
    present = Present()
    present.wrap(44)
    with pytest.raises(Exception) as e:
        present.wrap(54)
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."