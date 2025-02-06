import requests
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options



@pytest.fixture()
def driver():
    #options = Options()
    #options.add_argument('--headless')
    #driver = webdriver.Chrome(options=options)
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(3)
    print ("Before test")
    yield driver
    #driver.close()
    driver.quit()

@pytest.fixture(scope="module")
def testit_setup():
    api_token = "T0FLQjNKMzdPd1A3b1NpYzN5"
    base_url = "https://team-v5ka.testit.software"
    testit = TestIT(api_token, base_url)
    return testit


class TestIT:
    def __init__(self, api_token, base_url):
        self.api_token = api_token
        self.base_url = base_url

    def get_test_case(self, test_case_id):
        headers = {
            "Authorization": f"Bearer {self.api_token}"
        }
        response = requests.get(f"{self.base_url}/api/test-cases/{test_case_id}", headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to retrieve test case: {response.content}")