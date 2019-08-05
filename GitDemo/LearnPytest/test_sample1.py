import pytest
# def test_file1method1():
#     x=5
#     y=6
#     assert x+y==11,"test passed"
#     # assert x+1==1,"test failed"
#
# def test_file1method2():
#     x=3
#     y=2
#     assert x+1==1,"test failed"

@ pytest.mark.set1
def test_m1():
    a,b=2,3
    assert a*b==7,'failed'

@ pytest.mark.set2
def test_m2():
    a,b=2,5
    assert a+1==3,'passed'
