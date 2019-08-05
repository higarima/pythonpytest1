import pytest
def test_m1(supply_in_conftest1):
    x=3
    assert supply_in_conftest1[0]==x,'passed'