import os
import pytest
import allure
from selenium import webdriver

# Фикстура для создания драйвера браузера
@pytest.fixture(scope='function', autouse=True)
def driver():
    d = webdriver.Chrome()
    d.maximize_window()
    d.implicitly_wait(3)
    yield d
    d.quit()

def take_screenshot(driver, test_name):
    print(f"Taking screenshot for: {test_name}...")
    if not os.path.exists('screenshots'):
        os.makedirs('screenshots')
        print("Created screenshots directory.")

    screenshot_path = f'screenshots/{test_name}.png'
    try:
        driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved to: {screenshot_path}")
        allure.attach.file(screenshot_path, name='Screenshot', attachment_type=allure.attachment_type.PNG)
    except Exception as e:
        print(f'Failed to save screenshot: {e}')


# Вызов отладочной печати в pytest_runtest_makereport:
def pytest_runtest_makereport(item, call):
    if call.when == "call":
        if call.excinfo:
            print(f"Test {item.name} failed with exception: {call.excinfo}")
            take_screenshot(item.funcargs['driver'], item.name)