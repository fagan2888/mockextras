from matchers import Any, Contains


def test_any_equality():
    assert Any() == "hello"
    assert "hello" == Any()
    
    assert Any() == []
    assert [] == Any() 
    
    assert Any() == 100
    assert 100 == Any() 
    
    assert Any() == []
    assert [] == Any() 
    
    assert Any() == 100
    assert 100 == Any() 
    
    assert Any(str) == "hello"
    assert "hello" == Any(str)
    
    assert Any(list) != "hello"
    assert "hello" != Any(list)
    
    assert Any(list) == []
    assert [] == Any(list) 


def test_pretty_print_any():
    a = Any()
    assert repr(a) == "Any()"
    assert str(a) == "Any()"
    b = Any(str)
    assert repr(b) == "Any(<type 'str'>)"
    assert str(b) == "Any(<type 'str'>)"
    
    
def test_contains_equality():
    assert Contains('h') == "hello"
    assert Contains('hell') == "hello"
    assert Contains('hello world') != "hello"
    assert Contains('fish') != "hello"
    
    assert "hello" == Contains('h')
    assert "hello" == Contains('hell')
    assert "hello" != Contains('hello world')
    assert "hello" != Contains('fish')
    
    assert range(100) == Contains(25)
    assert range(100) != Contains(125)
    
    assert dict(a=1, b=2, c=3) == Contains('a')
    assert dict(a=1, b=2, c=3) != Contains('d')
    assert Contains('a') == dict(a=1, b=2, c=3)
    assert Contains('d') != dict(a=1, b=2, c=3)


def test_pretty_print_contains():
    a = Contains(10)
    assert repr(a) == "Contains(10)"
    assert str(a) == "Contains(10)"
    
    b = Contains('hello')
    assert repr(b) == "Contains('hello')"
    assert str(b) == "Contains('hello')"