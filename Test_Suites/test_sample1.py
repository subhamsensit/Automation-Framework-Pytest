import pytest

@pytest.fixture(scope="module")
def my_fixture(scope="module"): # this will make this scope in module level
    print("this is fixture function")
    yield
    print("this code is after execution of the test case")

#@pytest.mark.regression
@pytest.mark.skip("This release skipping the test case")
def test_1(my_fixture):
    print("sample testing 1 ")
    assert 10==20,"value error 10 is not equal to 20"
@pytest.mark.sanity
def test_2(my_fixture):
    print("sample testing 2")
    assert 10==10