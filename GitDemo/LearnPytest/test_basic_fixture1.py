import pytest
@pytest.fixture
def supply_ABC():
    a=1
    b=2
    c=3
    return [a,b,c]

def test_A(supply_ABC):
    x=2
    assert supply_ABC[0]==x,'failed'

def test_B(supply_ABC):
    y=2
    assert supply_ABC[1]==y,'passed'

def test_C(supply_ABC):
    z=4
    assert supply_ABC[2]==z,'failed'
