import pytest
# def test_method1():
#     a=2
#     b=3
#     assert a+b==5,"test passed"
# def test_method2():
#     a,b=2,4
#     assert a+1==4,'failed'

@pytest.mark.set1
def test_m1():
    a,c=2,6
    assert a+c==8,'passed'

@pytest.mark.set2
def test_m2():
    a=3
    assert a+1==4,'i  am pass'

