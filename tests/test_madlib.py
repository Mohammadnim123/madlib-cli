from madlib_cli.madlib import read_template,merge,parse

def test_read_template():
    expected = "banana"
    actual = read_template("         banana      ")
    assert expected == actual

def test_merge():
    x = """
    Madlib Game
    %s on the %s and he %s from LTUC students
    so he will %s on his face.
    """
    y = ["ali","tree","afraid","hit"]
    expected = """
    Madlib Game
    ali on the tree and he afraid from LTUC students
    so he will hit on his face.
    """
    actual = merge(x,y)
    assert expected == actual


def test_parse():
    x = """
    Madlib Game
    %s on the %s and he %s from LTUC students
    so he will %s on his face.
    """
    
    expected = ['\n    Madlib Game\n     on the  and he  from LTUC students\n    so he will  on his face.\n    ', ['%s', '%s', '%s', '%s']]
    actual = parse(x)
    assert expected == actual