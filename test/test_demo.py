import random
import pytest

@pytest.fixture()
def before_after():
    print ("Before test")
    yield  None
    print("\nAfter test")

from random import choice

my_list = ["text", "one", "two"]

print(random.choice(my_list))

def test_demo1():
    assert 1==1

def test_demo2(before_after):
    assert 2==2