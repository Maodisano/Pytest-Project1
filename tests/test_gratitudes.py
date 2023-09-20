from lib.gratitudes import *

#check that initially check that a no input creates a list

def test_gratitudes_are_empty_list():
    gratitudes = Gratitudes()
    assert gratitudes.format() == "Be grateful for: "

#test to see if a single input will append the list

def test_single_gratitude_appends_list():
    gratitudes = Gratitudes()
    gratitudes.add("money")
    assert gratitudes.format() == "Be grateful for: money"

#test to see if multiple inputs will add gratitudes to the list

def test_multiple_gratitudes_appends_list():
    gratitudes = Gratitudes()
    gratitudes.add("money")
    gratitudes.add("fame")
    gratitudes.add("power")
    assert gratitudes.format() == "Be grateful for: money, fame, power"
    
