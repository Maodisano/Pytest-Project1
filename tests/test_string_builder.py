

from lib.string_builder import *

# initial output is an empty string

def test_inital_output_is_empty_string():
    string_builder = StringBuilder()
    assert string_builder.output() == ""

#when we add a single string the output is now that string

def test_adding_a_string_outputs_string():
    string_builder = StringBuilder()
    string_builder.add("beauty")
    result = string_builder.output()
    assert result == "beauty"

#test when we add a single string - returns len of string

def test_single_sting_outputs_length():
    string_builder = StringBuilder()
    string_builder.add("beauty")
    assert string_builder.size() == 6

#test if when adding multiple strings - output is those stringes concatonated

def test_multiple_strings_return_concatonated():
    string_builder = StringBuilder()
    string_builder.add("beauty")
    string_builder.add(" intelligence")
    string_builder.add(" craze")
    assert string_builder.output() == "beauty intelligence craze"

#the size is the size of all the strings added

def test_multiple_strings_return_accurate_size():
    string_builder = StringBuilder()
    string_builder.add("beauty")
    string_builder.add(" intelligence")
    string_builder.add(" craze")
    assert string_builder.size() == 25



