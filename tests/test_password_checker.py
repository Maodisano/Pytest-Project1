
from lib.password_checker import *
import pytest

# test if password is larger than 8 characers - return false

def test_check_password_is_more_than_8():
    password = PasswordChecker()
    assert password.check("bootlicker") == True

# test is password is smaller than 8 characters 

def test_check_password_is_less_than_8():
    password = PasswordChecker()
    with pytest.raises(Exception) as e:
        password.check("booty")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."