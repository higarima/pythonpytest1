import pytest
def test_file1method1():
    x=5
    y=6
    assert x+y==11,"test passed"
    # assert x+1==1,"test failed"

def test_file1method2():
    x=3
    y=2
    assert x+1==1,"test failed"