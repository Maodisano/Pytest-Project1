
from lib.counter import *

#test each of the functions
# initially, reports a count of zero



def test_counter_initiallly_reports_0():
    counter = Counter()
    assert counter.report() == "Counted to 0 so far."

#test if the counter will add a number to the report 

def test_adds_sing_number_to_count():
    counter = Counter()
    counter.add(5)
    assert counter.report() == "Counted to 5 so far."

#test if when we add multiple numbers to the counter - sum of those numbers are reflected in the report

def test_counter_adds_multiple_numbers_to_count():
    counter = Counter()
    counter.add(8)
    counter.add(2)
    assert counter.report() == "Counted to 10 so far."
    