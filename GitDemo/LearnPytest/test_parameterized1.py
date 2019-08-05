import pytest
@pytest.mark.parametrize('input1, input2, output',[(1,3,4),(3,5,8)])
def test_add(input1, input2, output):
    assert input1+input2==output,'failed'
