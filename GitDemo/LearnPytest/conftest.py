import pytest
@pytest.fixture
def supply_in_conftest1():
    a=3
    b=4
    c=5
    return [a,b,c]
