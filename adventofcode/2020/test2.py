# content of test_sample.py
def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 4
    
    
def f():
    raise SystemExit(1)

# content of test_sysexit.py
import pytest

def test_mytest():
    with pytest.raises(SystemExit):
        f()



class TestClass:
    age = 23
    name = 'Adam'

    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(TestClass, "age")


@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 54)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected