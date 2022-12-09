import pytest


actual_result = "Hello"


@pytest.mark.TopPriority
@pytest.mark.Regression
def test_tc_001_Login_Logout_Testing():
    print("This is Smoke Test Case..")
    print("This is and of my test cases")
    assert actual_result != "Testing", "These 2 values must not be same"


@pytest.mark.Sanity
@pytest.mark.Regression
def test_tc_002_Login_Logout_Invalid_Credentials():
    print("This is Smoke Test Case..")
    print("This is and of my test cases")
    assert actual_result == "Hello"
