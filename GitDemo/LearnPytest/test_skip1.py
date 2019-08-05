import pytest
@pytest.mark.skip
def test_m1():
    a=1
    assert a+1==3,'failed'
def test_m2():
    a=2
    assert a-1==1,'pass'
@pytest.mark.xfail
def test_add():
    a=2
    b=4
    assert a+b==6,'pass but skip'