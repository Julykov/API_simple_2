import pytest


@pytest.fixture(scope='module')
def fixture_code_module():
    print()
    print("This is our fixture Code will execute once before all testcases")
    print("========================================================================================")
    yield
    print("Close browser after executing testcase of Close DB connection once after executing all testcases")
    print("========================================================================================")


@pytest.fixture(scope='function')
def fixture_code_function():
    print()
    print("This is our fixture Code will execute before eachtestcase")
    print("-----------------------------------------------------")
    yield
    print("This is our fixture Code will execute after eachtestcase")
    print("-----------------------------------------------------")


@pytest.mark.Smoke
@pytest.mark.Regression
def test_tc_001_Login_Logout_Testing(fixture_code_function, fixture_code_module):
    print("This is Smoke Test Case..")
    print("This is end of my test cases")


@pytest.mark.Sanity
@pytest.mark.Regression
def test_tc_002_Login_Logout_Invalid_Credentials(fixture_code_function, fixture_code_module):
    print("This is Smoke Test Case..")
    print("This is end of my test cases")
