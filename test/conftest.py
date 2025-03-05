import os
import pytest
import allure
from selenium import webdriver

from constants import URLs, subURLs


# Фикстура для создания драйвера браузера
@pytest.fixture(scope='function', autouse=True)
def driver():
    d = webdriver.Chrome()
    d.maximize_window()
    d.implicitly_wait(3)
    yield d
    d.quit()

@pytest.fixture(params=[
    {
        "page": "main",
        "title": "Web Development Company in USA | Web Design, App & Web Development Services – Godev",
        "description": "Godev is a leading web development company in the USA. We specialize in custom web design, web applications, app and web development services",
        "canonical": URLs.MAIN_PAGE
    },
    {
        "page": "services",
        "title": "IT services for you and your business",
        "description": "In godev studio you can order the creation of a website, portal or application of any complexity. We use a wide technology stack",
        "canonical": URLs.MAIN_PAGE+subURLs.SERVICES_PAGE
    },
    {
        "page": "cms",
        "title": "Custom CMS Development Services in USA: Company for Your Website Needs",
        "description": "Unlock your website's potential with our custom CMS development services in the USA. Tailored solutions to meet your business needs, backed by years of Godev's experience",
        "canonical": URLs.MAIN_PAGE+subURLs.CMS_PAGE
    },
    {
        "page": "b2b",
        "title": "B2B Ecommerce Website Development Services in USA: Design Strategies for Success with Godev",
        "description": "Transform your B2B ecommerce website with Godev's expert design strategies. Our web development services create high-converting platforms for success",
        "canonical": URLs.MAIN_PAGE+subURLs.B2B_PAGE
    },
    {
        "page": "mobile",
        "title": "Mobile App Development Services in USA, Leading Mobile Application Development Company Godev",
        "description": "Transform your ideas into reality with our mobile app development services. As a leading mobile app development company, we specialize in custom solutions for iOS and Android, including cross-platform apps",
        "canonical": URLs.MAIN_PAGE+subURLs.MOBILE_PAGE
    },
    {
        "page": "blog",
        "title": "",
        "description": "",
        "canonical": URLs.MAIN_PAGE+subURLs.BLOG_PAGE
    },
    {
        "page": "framework",
        "title": "Web Development on Frameworks in the USA: website development in Godev",
        "description": "Explore top web development frameworks in the USA with Godev. Save time and enhance coding efficiency for your projects by leveraging powerful software infrastructure!",
        "canonical": URLs.MAIN_PAGE+subURLs.FRAMEWORK_PAGE
    },
    {
        "page": "outstaff",
        "title": "IT staff augmentation company in USA, cost of outsorce tech teams and software developers",
        "description": "IT staff augmentation – hire tech teams and software developers for your projects with lower cost in USA. Software, databases, websites, applications, microservices, mobile applications",
        "canonical": URLs.MAIN_PAGE+subURLs.OUTSTAFFING
    },
    {
        "page": "project_page",
        "title": "Web Development and Designs Portfolio - Godev",
        "description": "Godev's portfolio consist of completed projects in Design and Web Development. We help clients grow and prosper for over 10 years",
        "canonical": URLs.MAIN_PAGE+subURLs.PROJECT_PAGE
    },
    {
        "page": "reviews",
        "title": "Godev Reviews | Web development in USA",
        "description": "Reviews from our clients about web development with Godev",
        "canonical": URLs.MAIN_PAGE+subURLs.REVIEWS_PAGE
    },
    {
        "page": "support",
        "title": "IT maintenance and support services in USA",
        "description": "Discover top-notch IT maintenance and support services in the USA, ensuring your software and applications run smoothly with timely updates and expert assistance Godev",
        "canonical": URLs.MAIN_PAGE+subURLs.SUPPORT_PAGE
    },
    {
        "page": "web_dev_serv",
        "title": "Web Development Services in USA, Custom Website and Web App Development Solutions | Godev",
        "description": "Looking for expert web development services in the USA? Godev offers high-quality, custom website development and responsive web design solutions tailored to your needs.",
        "canonical": URLs.MAIN_PAGE+subURLs.WEB_DEV
    },
    {
        "page": "web_dev",
        "title": "Website Development Company in USA, Leading Web Design and Development Services Godev",
        "description": "Discover Godev, a leading web development company in the USA, offering top-notch web design and development services to elevate your online business. Professional web developers with 10+ years of experience.",
        "canonical": URLs.MAIN_PAGE+subURLs.WEBSITE_DEV
    },
    {
        "page": "landing",
        "title": "Mastering Landing Page Design in USA, Top Development Services in Godev",
        "description": "Unlock the secrets to effective landing page design in the USA with Godev's top development services. Generate more leads and enhance conversions today!",
        "canonical": URLs.MAIN_PAGE+subURLs.LANDING
    }

])

def meta_data(request):
    return request.param

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

# Вызов отладочной печати
def pytest_runtest_makereport(item, call):
    if call.when == "call":
        if call.excinfo:
            print(f"Test {item.name} failed with exception: {call.excinfo}")
            take_screenshot(item.funcargs['driver'], item.name)

@pytest.fixture(params=[
        ("1", URLs.MAIN_PAGE + subURLs.E_COM_PAGE, "E-commerce web development for scalable business growth"),
        ("2", URLs.MAIN_PAGE + subURLs.B2B_PAGE, "B2B e-commerce website development"),
        ("3", URLs.MAIN_PAGE + subURLs.FRAMEWORK_PAGE, "What is a framework and why it’s essential for web development")
    ])
def test_data(request):
    return request.param

@pytest.fixture(params=[
    ("1", URLs.MAIN_PAGE + subURLs.B2B_PAGE, "B2B e-commerce website development"),
    ("2", URLs.MAIN_PAGE + subURLs.CMS_PAGE, "Custom CMS development service"),
    ("3", URLs.MAIN_PAGE + subURLs.FRAMEWORK_PAGE, "What is a framework and why it’s essential for web development")
])
def test_data_cards(request):
    return request.param

