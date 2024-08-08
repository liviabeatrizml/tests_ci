from src.minhabib import fat

def test_fat():
    assert (fat(5) == 120) == True
    assert (fat(2) == 4) == False
    assert (fat(6) == 2) == False
