
from lib.check_codeword import *



# if the codeword is correct - returns entry string
# if codeword contains H and E (start and end) then return almost string
# if codeword is incorrect return WRONG

def test_with_correct_codeword():

    result = check_codeword("horse")
    assert result == "Correct! Come in."

def test_with_incorrect_codeword():
    result = check_codeword("water")
    assert result == "WRONG!"

def test_with_first_and_last_codeword():

    result = check_codeword("house")
    assert result == "Close, but nope."
