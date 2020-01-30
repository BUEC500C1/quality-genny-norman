from arabicToRomanConv import conversion

def test_basic():
    assert conversion(55) == "LV"

def test_alpha():
    assert conversion('asdjf') == ""

def test_zero():
    assert conversion(0) == ""

def test_fours():
    assert conversion(14) == "XIV"

def test_nines():
    assert conversion(99) == "XCIX"

def test_decimal():
    assert conversion(12.3) == ""

def test_negative():
    assert conversion(-4) == ""
