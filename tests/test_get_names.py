from lib.get_names import get_names

# 
def test_one_name_returns_single():
    assert get_names(["Bart"]) == "Bart"

def test_two_names_returns_and():
    assert get_names(["Bart", "Lisa"]) == "Bart & Lisa"

def test_multiple_names():
    assert  get_names(["Bart", "Lisa", "Maggie"]) == "Bart, Lisa & Maggie"

def test_empty_list():
    assert get_names([]) == ""