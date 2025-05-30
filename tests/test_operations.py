from src.math_operations import add,sub

def test_add():
    assert add(2,4) == 6
    assert add(-1,1) == 0
    assert add(120,34.5) == 154.5
    
def test_sub():
    assert sub(5,3) == 2
    assert sub(3,5) == -2
    