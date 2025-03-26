import os

import pytest
from allure_commons._allure import link

from pages.base_page import put_a_secret
from pages.main_page import MainPage


@link(url='https://team-v5ka.testit.software/projects/664/tests/767',
      name='Проверка открытия страниц из верхнеуровнего меню - главная')
@pytest.mark.prod_test
def test_menu_services_click_and_open_page(driver):
    main_page_test = MainPage(driver)
    main_page_test.open()
    menu_elements = main_page_test.get_menu_element()
    menu_elements.click_menu_service()
    assert driver.current_url == put_a_secret() + os.getenv('SERVICES_PAGE',
                                                            'services/'), f"Ожидался URL '{put_a_secret() + os.getenv('SERVICES_PAGE', 'services/')}', но получен '{driver.current_url}'"


@link(url='https://team-v5ka.testit.software/projects/664/tests/767',
      name='Проверка открытия страниц из верхнеуровнего меню - проекты')
@pytest.mark.prod_test
def test_menu_project_click_and_open_page(driver):
    main_page_test = MainPage(driver)
    main_page_test.open()
    menu_elements = main_page_test.get_menu_element()
    menu_elements.click_menu_project()
    assert driver.current_url == put_a_secret() + os.getenv('PROJECT_PAGE',
                                                            'projects/'), f"Ожидался URL '{put_a_secret() + os.getenv('PROJECT_PAGE', 'projects/')}', но получен '{driver.current_url()}'"


@link(url='https://team-v5ka.testit.software/projects/664/tests/767',
      name='Проверка открытия страниц из верхнеуровнего меню - отзывы')
@pytest.mark.prod_test
def test_menu_reviews_click_and_open_page(driver):
    main_page_test = MainPage(driver)
    main_page_test.open()
    menu_elements = main_page_test.get_menu_element()
    menu_elements.click_menu_reviews()
    assert driver.current_url == put_a_secret() + os.getenv('REVIEWS_PAGE',
                                                            'reviews/'), f"Ожидался URL '{put_a_secret() + os.getenv('REVIEWS_PAGE', 'reviews/')}', но получен '{driver.current_url()}'"


@link(url='https://team-v5ka.testit.software/projects/664/tests/767',
      name='Проверка открытия страниц из верхнеуровнего меню - контакты')
@pytest.mark.prod_test
def test_menu_contacts_click_and_open_page(driver):
    main_page_test = MainPage(driver)
    main_page_test.open()
    menu_elements = main_page_test.get_menu_element()
    menu_elements.click_menu_contacts()
    assert driver.current_url == put_a_secret() + os.getenv('CONTACTS',
                                                            'contacts/'), f"Ожидался URL '{put_a_secret() + os.getenv('CONTACTS', 'contacts/')}]', но получен '{driver.current_url()}'"


@link(url='https://team-v5ka.testit.software/projects/664/tests/768',
      name='Проверка открытия меню второго уровня - сабменю itStaff')
@pytest.mark.prod_test
def test_submenu_outstaff_click_and_open_page(driver):
    main_page_test = MainPage(driver)
    main_page_test.open()
    menu_elements = main_page_test.get_menu_element()
    menu_elements.click_submenu_outstaff()
    assert driver.current_url == put_a_secret() + os.getenv('OUTSTAFFING',
                                                            'services/outstaffing-and-outsourcing-of-it-specialists/'), f"Ожидался URL '{put_a_secret() + os.getenv('OUTSTAFFING', 'services/outstaffing-and-outsourcing-of-it-specialists/')}', но получен '{driver.current_url()}'"


@link(url='https://team-v5ka.testit.software/projects/664/tests/768',
      name='Проверка открытия меню второго уровня - сабменю mobile')
@pytest.mark.prod_test
def test_submenu_mobile_click_and_open_page(driver):
    main_page_test = MainPage(driver)
    main_page_test.open()
    menu_elements = main_page_test.get_menu_element()
    menu_elements.click_submenu_mobile_dev()
    assert driver.current_url == put_a_secret() + os.getenv('MOBILE_PAGE',
                                                            'services/mobile-development/'), f"Ожидался URL '{put_a_secret() + os.getenv('MOBILE_PAGE', 'services/mobile-development/')}', но получен '{driver.current_url()}'"


@link(url='https://team-v5ka.testit.software/projects/664/tests/768',
      name='Проверка открытия меню второго уровня - сабменю web_site_dev')
@pytest.mark.prod_test
def test_submenu_web_site_dev_click_and_open_page(driver):
    main_page_test = MainPage(driver)
    main_page_test.open()
    menu_elements = main_page_test.get_menu_element()
    menu_elements.click_submenu_web_site_dev()
    assert driver.current_url == put_a_secret() + os.getenv('WEBSITE_DEV',
                                                            'services/website-development/'), f"Ожидался URL '{put_a_secret() + os.getenv('WEBSITE_DEV', 'services/website-development/')}', но получен '{driver.current_url()}'"


@link(url='https://team-v5ka.testit.software/projects/664/tests/768',
      name='Проверка открытия меню второго уровня - сабменю web_dev')
@pytest.mark.prod_test
def test_submenu_web_development_click_and_open_page(driver):
    main_page_test = MainPage(driver)
    main_page_test.open()
    menu_elements = main_page_test.get_menu_element()
    menu_elements.click_submenu_web_dev()
    assert driver.current_url == put_a_secret() + os.getenv('WEB_DEV',
                                                            'services/web-development/'), f"Ожидался URL '{put_a_secret() + os.getenv('WEB_DEV', 'services/web-development/')}', но получен '{driver.current_url()}'"


@link(url='https://team-v5ka.testit.software/projects/664/tests/768',
      name='Проверка открытия меню второго уровня - сабменю tech_support')
@pytest.mark.prod_test
def test_submenu_tech_support_click_and_open_page(driver):
    main_page_test = MainPage(driver)
    main_page_test.open()
    menu_elements = main_page_test.get_menu_element()
    menu_elements.click_submenu_tech_support()
    assert driver.current_url == put_a_secret() + os.getenv('SUPPORT_PAGE',
                                                            'services/tech-support/'), f"Ожидался URL '{put_a_secret() + os.getenv('SUPPORT_PAGE', 'services/tech-support/')}', но получен '{driver.current_url()}'"


@link(url='https://team-v5ka.testit.software/projects/664/tests/769',
      name='Проверка открытия меню второго уровня - сабменю e_com')
@pytest.mark.prod_test
def test_submenu_e_com_click_and_open_page(driver):
    main_page_test = MainPage(driver)
    main_page_test.open()
    menu_elements = main_page_test.get_menu_element()
    menu_elements.click_submenu_e_com()
    assert driver.current_url == put_a_secret() + os.getenv('E_COM_PAGE',
                                                            'services/website-development/e-commerce/'), f"Ожидался URL '{put_a_secret() + os.getenv('E_COM_PAGE', 'services/website-development/e-commerce/')}', но получен '{driver.current_url()}'"


@link(url='https://team-v5ka.testit.software/projects/664/tests/769',
      name='Проверка открытия меню второго уровня - сабменю cms')
@pytest.mark.prod_test
def test_submenu_cms_click_and_open_page(driver):
    main_page_test = MainPage(driver)
    main_page_test.open()
    menu_elements = main_page_test.get_menu_element()
    menu_elements.click_submenu_cms()
    assert driver.current_url == put_a_secret() + os.getenv('CMS_PAGE',
                                                            'services/website-development/cms/'), f"Ожидался URL '{put_a_secret() + os.getenv('CMS_PAGE', 'services/website-development/cms/')}, но получен '{driver.current_url()}'"


@link(url='https://team-v5ka.testit.software/projects/664/tests/769',
      name='Проверка открытия меню второго уровня - сабменю framework')
@pytest.mark.prod_test
def test_submenu_framework_click_and_open_page(driver):
    main_page_test = MainPage(driver)
    main_page_test.open()
    menu_elements = main_page_test.get_menu_element()
    menu_elements.click_submenu_framework()
    assert driver.current_url == put_a_secret() + os.getenv('FRAMEWORK_PAGE',
                                                            'services/website-development/framework/'), f"Ожидался URL '{put_a_secret() + os.getenv('FRAMEWORK_PAGE', 'services/website-development/framework/')}, но получен '{driver.current_url()}'"


@link(url='https://team-v5ka.testit.software/projects/664/tests/769',
      name='Проверка открытия меню второго уровня - сабменю b2b')
@pytest.mark.prod_test
def test_submenu_b2b_click_and_open_page(driver):
    main_page_test = MainPage(driver)
    main_page_test.open()
    menu_elements = main_page_test.get_menu_element()
    menu_elements.click_submenu_b2b()
    assert driver.current_url == put_a_secret() + os.getenv('B2B_PAGE',
                                                            'services/website-development/b2b/'), f"Ожидался URL '{put_a_secret() + os.getenv('B2B_PAGE', 'services/website-development/b2b/')}, но получен '{driver.current_url()}'"


@link(url='https://team-v5ka.testit.software/projects/664/tests/769',
      name='Проверка открытия меню второго уровня - сабменю landing')
@pytest.mark.prod_test
def test_submenu_landing_click_and_open_page(driver):
    main_page_test = MainPage(driver)
    main_page_test.open()
    menu_elements = main_page_test.get_menu_element()
    menu_elements.click_submenu_landing()
    assert driver.current_url == put_a_secret() + os.getenv('LANDING',
                                                            'services/development-of-a-landing-page/'), f"Ожидался URL '{put_a_secret() + os.getenv('LANDING', 'services/development-of-a-landing-page/')}, но получен '{driver.current_url()}'"
