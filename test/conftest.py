import argparse
import logging
import os
import pytest
import allure
import requests
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# Фикстура для создания драйвера браузера
def pytest_addoption(parser):
    parser.addoption('--headless',
                     action='store_true',
                     default=None,
                     help='Run tests in headless mode')


@pytest.fixture(scope='function', autouse=True)
def driver(request):
    chrome_options = Options()

    # Установка стратегии загрузки страницы
    chrome_options.page_load_strategy = 'eager'  # Ожидание загрузки DOM

    # Проверяем условия для headless режима
    run_headless = (
            request.config.getoption('--headless') or  # параметр --headless
            os.getenv('CI') or  # CI/CD окружение
            os.getenv('HEADLESS')  # переменная окружения
    )

    if run_headless:
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--window-size=1920,1080')  # фиксированный размер в headless

    # Общие опции
    chrome_options.add_argument('--disable-notifications')
    chrome_options.add_argument('--disable-infobars')
    chrome_options.add_argument('--start-maximized')

    # Дополнительные опции для CI/CD
    if os.getenv('CI'):
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument('--disable-dev-tools')

    # Инициализация драйвера
    d = webdriver.Chrome(options=chrome_options)

    if not run_headless:
        d.maximize_window()

    d.implicitly_wait(3)
    yield d
    d.quit()


def verify_recaptcha(response):
    secret_key = 'YOUR_SECRET_KEY'
    payload = {
        'secret': secret_key,
        'response': response
    }

    try:
        response = requests.post('https://www.google.com/recaptcha/api/siteverify', data=payload)
        result = response.json()

        if result.get('success') and result.get('score', 0) >= 0.5:
            return True
        else:
            return False
    except requests.RequestException as e:
        # Логирование ошибки
        print(f"Error during reCAPTCHA verification: {e}")
        return False

def put_a_secret():
    # Получаем значение окружения
    environment = os.getenv('ENVIRONMENT', 'production')  # Значение по умолчанию - development (второе значение - production)
    # Определяем базовый URL в зависимости от окружения
    if environment == 'production':
        base_url = os.getenv('PROD_PAGE', 'https://godev.agency/')  # Значение по умолчанию для прод окружения
    else:
        base_url = os.getenv('MAIN_PAGE', 'https://dev.godev.agency/')  # Значение по умолчанию для дев окружения
    return base_url

@pytest.fixture(params=[
    {
        "page": "main",
        "title": "Web Development Company in USA | Web Design, App & Web Development Services – Godev",
        "description": "Godev is a leading web development company in the USA. We specialize in custom web design, web applications, app and web development services",
        "canonical": put_a_secret()
    },
    {
        "page": "services",
        "title": "IT services for you and your business",
        "description": "In godev studio you can order the creation of a website, portal or application of any complexity. We use a wide technology stack",
        "canonical": put_a_secret() + os.getenv('SERVICES_PAGE', 'services/')
    },
    {
        "page": "cms",
        "title": "Custom CMS Development Services in USA: Company for Your Website Needs",
        "description": "Unlock your website's potential with our custom CMS development services in the USA. Tailored solutions to meet your business needs, backed by years of Godev's experience",
        "canonical": put_a_secret() + os.getenv('CMS_PAGE', 'services/website-development/cms/')
    },
    {
        "page": "b2b",
        "title": "B2B Ecommerce Website Development Services in USA: Design Strategies for Success with Godev",
        "description": "Transform your B2B ecommerce website with Godev's expert design strategies. Our web development services create high-converting platforms for success",
        "canonical": put_a_secret() + os.getenv('B2B_PAGE', 'services/website-development/b2b/')
    },
    {
        "page": "mobile",
        "title": "Mobile App Development Services in USA, Leading Mobile Application Development Company Godev",
        "description": "Transform your ideas into reality with our mobile app development services. As a leading mobile app development company, we specialize in custom solutions for iOS and Android, including cross-platform apps",
        "canonical": put_a_secret() + os.getenv('MOBILE_PAGE', 'services/mobile-development/')
    },
    #{
        #"page": "blog",
        #"title": "",
        #"description": "",
        #"canonical": put_a_secret() + os.getenv('BLOG_PAGE', 'blog/')
    #},
    {
        "page": "framework",
        "title": "Web Development on Frameworks in the USA: website development in Godev",
        "description": "Explore top web development frameworks in the USA with Godev. Save time and enhance coding efficiency for your projects by leveraging powerful software infrastructure!",
        "canonical": put_a_secret() + os.getenv('FRAMEWORK_PAGE', 'services/website-development/framework/')
    },
    {
        "page": "outstaff",
        "title": "IT staff augmentation company in USA, cost of outsorce tech teams and software developers",
        "description": "IT staff augmentation – hire tech teams and software developers for your projects with lower cost in USA. Software, databases, websites, applications, microservices, mobile applications",
        "canonical": put_a_secret() + os.getenv('OUTSTAFFING', 'services/outstaffing-and-outsourcing-of-it-specialists/')
    },
    {
        "page": "project_page",
        "title": "Web Development and Designs Portfolio - Godev",
        "description": "Godev's portfolio consist of completed projects in Design and Web Development. We help clients grow and prosper for over 10 years",
        "canonical": put_a_secret() + os.getenv('PROJECT_PAGE', 'projects/')
    },
    {
        "page": "reviews",
        "title": "Godev Reviews | Web development in USA",
        "description": "Reviews from our clients about web development with Godev",
        "canonical": put_a_secret() + os.getenv('REVIEWS_PAGE', 'reviews/')
    },
    {
        "page": "support",
        "title": "IT maintenance and support services in USA",
        "description": "Discover top-notch IT maintenance and support services in the USA, ensuring your software and applications run smoothly with timely updates and expert assistance Godev",
        "canonical": put_a_secret() + os.getenv('SUPPORT_PAGE', 'services/tech-support/')
    },
    {
        "page": "web_dev_serv",
        "title": "Web Development Services in USA, Custom Website and Web App Development Solutions | Godev",
        "description": "Looking for expert web development services in the USA? Godev offers high-quality, custom website development and responsive web design solutions tailored to your needs.",
        "canonical": put_a_secret() + os.getenv('WEB_DEV', 'services/web-development/')
    },
    {
        "page": "web_dev",
        "title": "Website Development Company in USA, Leading Web Design and Development Services Godev",
        "description": "Discover Godev, a leading web development company in the USA, offering top-notch web design and development services to elevate your online business. Professional web developers with 10+ years of experience.",
        "canonical": put_a_secret() + os.getenv('WEBSITE_DEV', 'services/website-development/')
    },
    {
        "page": "landing",
        "title": "Mastering Landing Page Design in USA, Top Development Services in Godev",
        "description": "Unlock the secrets to effective landing page design in the USA with Godev's top development services. Generate more leads and enhance conversions today!",
        "canonical": put_a_secret() + os.getenv('LANDING', 'services/development-of-a-landing-page/')
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
        ("1", put_a_secret() + os.getenv('E_COM_PAGE', 'services/website-development/e-commerce/'), "E-commerce web development for scalable business growth"),
        ("2", put_a_secret() + os.getenv('B2B_PAGE', 'services/website-development/b2b/'), "B2B e-commerce website development"),
        ("3", put_a_secret() + os.getenv('FRAMEWORK_PAGE', 'services/website-development/framework/'), "What is a framework and why it’s essential for web development")
    ])
def test_data(request):
    return request.param

@pytest.fixture(params=[
    ("1", put_a_secret() + os.getenv('B2B_PAGE', 'services/website-development/b2b/'), "B2B e-commerce website development"),
    ("2", put_a_secret() + os.getenv('CMS_PAGE', 'services/website-development/cms/'), "Custom CMS development service"),
    ("3", put_a_secret() + os.getenv('FRAMEWORK_PAGE', 'services/website-development/framework/'), "What is a framework and why it’s essential for web development")
])
def test_data_cards(request):
    return request.param


# Загружаем переменные окружения из файла .env
load_dotenv()

class URLs:
    MAIN_PAGE = put_a_secret()
    PROD_PAGE = 'https://godev.agency/'
