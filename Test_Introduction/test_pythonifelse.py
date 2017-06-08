from Introduction import pythonifelse

def test_odd():
    assert pythonifelse.ifelse(3) == "Weird"
    assert pythonifelse.ifelse(99) == "Weird"
    assert pythonifelse.ifelse(69) == "Weird"
    assert pythonifelse.ifelse(5) == "Weird"
    assert pythonifelse.ifelse(15) == "Weird"

def test_even_in_range_2_5():
    assert pythonifelse.ifelse(2) == "Not Weird"
    assert pythonifelse.ifelse(4) == "Not Weird"

def test_even_in_range_6_20():
    assert pythonifelse.ifelse(6) == "Weird"
    assert pythonifelse.ifelse(8) == "Weird"
    assert pythonifelse.ifelse(10) == "Weird"
    assert pythonifelse.ifelse(12) == "Weird"
    assert pythonifelse.ifelse(14) == "Weird"
    assert pythonifelse.ifelse(16) == "Weird"
    assert pythonifelse.ifelse(18) == "Weird"
    assert pythonifelse.ifelse(20) == "Weird"

def test_even_greater_20():
    assert pythonifelse.ifelse(20) == "Weird"
    assert pythonifelse.ifelse(421) == "Not Weird"
    assert pythonifelse.ifelse(21) == "Not Weird"
    assert pythonifelse.ifelse(311) == "Not Weird"
    assert pythonifelse.ifelse(31) == "Not Weird"




