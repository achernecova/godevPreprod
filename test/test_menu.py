import allure
from allure_commons._allure import link

from constants import URLs, subURLs
from pages.main_page import MainPage

@link(url='https://team-v5ka.testit.software/projects/664/tests/767', name='Проверка открытия страниц из верхнеуровнего меню - главная')
def test_menu_services_click_and_open_page(driver):
    main_page_test = MainPage(driver)
    main_page_test.open()
    menu_elements = main_page_test.get_menu_element()
    menu_elements.click_menu_service()
    assert driver.current_url == URLs.MAIN_PAGE+subURLs.SERVICES_PAGE, f"Ожидался URL '{URLs.MAIN_PAGE+subURLs.SERVICES_PAGE}', но получен '{driver.current_url}'"

@link(url='https://team-v5ka.testit.software/projects/664/tests/767', name='Проверка открытия страниц из верхнеуровнего меню - проекты')
def test_menu_project_click_and_open_page(driver):
    main_page_test = MainPage(driver)
    main_page_test.open()
    menu_elements = main_page_test.get_menu_element()
    menu_elements.click_menu_project()
    assert driver.current_url == URLs.MAIN_PAGE+subURLs.PROJECT_PAGE, f"Ожидался URL '{URLs.MAIN_PAGE+subURLs.PROJECT_PAGE}', но получен '{driver.get_url()}'"

@link(url='https://team-v5ka.testit.software/projects/664/tests/767', name='Проверка открытия страниц из верхнеуровнего меню - отзывы')
def test_menu_reviews_click_and_open_page(driver):
    main_page_test = MainPage(driver)
    main_page_test.open()
    menu_elements = main_page_test.get_menu_element()
    menu_elements.click_menu_reviews()
    assert driver.current_url == URLs.MAIN_PAGE+subURLs.REVIEWS_PAGE, f"Ожидался URL '{URLs.MAIN_PAGE+subURLs.REVIEWS_PAGE}', но получен '{driver.get_url()}'"

@link(url='https://team-v5ka.testit.software/projects/664/tests/767', name='Проверка открытия страниц из верхнеуровнего меню - контакты')
def test_menu_contacts_click_and_open_page(driver):
    main_page_test = MainPage(driver)
    main_page_test.open()
    menu_elements = main_page_test.get_menu_element()
    menu_elements.click_menu_contacts()
    assert driver.current_url == URLs.MAIN_PAGE+subURLs.CONTACTS, f"Ожидался URL '{URLs.MAIN_PAGE+subURLs.CONTACTS}]', но получен '{driver.get_url()}'"


@link(url='https://team-v5ka.testit.software/projects/664/tests/768', name='Проверка открытия меню второго уровня - сабменю itStaff')
def test_submenu_outstaff_click_and_open_page(driver):
    main_page_test = MainPage(driver)
    main_page_test.open()
    menu_elements = main_page_test.get_menu_element()
    menu_elements.click_submenu_outstaff()
    assert driver.current_url == URLs.MAIN_PAGE+subURLs.OUTSTAFFING, f"Ожидался URL '{URLs.MAIN_PAGE+subURLs.OUTSTAFFING}', но получен '{driver.get_url()}'"

@link(url='https://team-v5ka.testit.software/projects/664/tests/768', name='Проверка открытия меню второго уровня - сабменю mobile')
def test_submenu_mobile_click_and_open_page(driver):
    main_page_test = MainPage(driver)
    main_page_test.open()
    menu_elements = main_page_test.get_menu_element()
    menu_elements.click_submenu_mobile_dev()
    assert driver.current_url == URLs.MAIN_PAGE+subURLs.MOBILE_PAGE, f"Ожидался URL '{URLs.MAIN_PAGE+subURLs.MOBILE_PAGE}', но получен '{driver.get_url()}'"

@link(url='https://team-v5ka.testit.software/projects/664/tests/768', name='Проверка открытия меню второго уровня - сабменю web_site_dev')
def test_submenu_web_site_dev_click_and_open_page(driver):
    main_page_test = MainPage(driver)
    main_page_test.open()
    menu_elements = main_page_test.get_menu_element()
    menu_elements.click_submenu_web_site_dev()
    assert driver.current_url == URLs.MAIN_PAGE+subURLs.WEBSITE_DEV, f"Ожидался URL '{URLs.MAIN_PAGE+subURLs.WEBSITE_DEV}', но получен '{driver.get_url()}'"

@link(url='https://team-v5ka.testit.software/projects/664/tests/768', name='Проверка открытия меню второго уровня - сабменю web_dev')
def test_submenu_web_development_click_and_open_page(driver):
    main_page_test = MainPage(driver)
    main_page_test.open()
    menu_elements = main_page_test.get_menu_element()
    menu_elements.click_submenu_web_dev()
    assert driver.current_url == URLs.MAIN_PAGE+subURLs.WEB_DEV, f"Ожидался URL '{URLs.MAIN_PAGE+subURLs.WEB_DEV}', но получен '{driver.get_url()}'"

@link(url='https://team-v5ka.testit.software/projects/664/tests/768', name='Проверка открытия меню второго уровня - сабменю tech_support')
def test_submenu_tech_support_click_and_open_page(driver):
    main_page_test = MainPage(driver)
    main_page_test.open()
    menu_elements = main_page_test.get_menu_element()
    menu_elements.click_submenu_tech_support()
    assert driver.current_url == URLs.MAIN_PAGE+subURLs.SUPPORT_PAGE, f"Ожидался URL '{URLs.MAIN_PAGE+subURLs.SUPPORT_PAGE}', но получен '{driver.get_url()}'"

@link(url='https://team-v5ka.testit.software/projects/664/tests/769', name='Проверка открытия меню второго уровня - сабменю e_com')
def test_submenu_e_com_click_and_open_page(driver):
    main_page_test = MainPage(driver)
    main_page_test.open()
    menu_elements = main_page_test.get_menu_element()
    menu_elements.click_submenu_e_com()
    assert driver.current_url == URLs.MAIN_PAGE+subURLs.E_COM_PAGE, f"Ожидался URL '{URLs.MAIN_PAGE+subURLs.E_COM_PAGE}', но получен '{driver.get_url()}'"

@link(url='https://team-v5ka.testit.software/projects/664/tests/769', name='Проверка открытия меню второго уровня - сабменю cms')
def test_submenu_cms_click_and_open_page(driver):
    main_page_test = MainPage(driver)
    main_page_test.open()
    menu_elements = main_page_test.get_menu_element()
    menu_elements.click_submenu_cms()
    assert driver.current_url == URLs.MAIN_PAGE+subURLs.CMS_PAGE, f"Ожидался URL '{URLs.MAIN_PAGE+subURLs.CMS_PAGE}, но получен '{driver.get_url()}'"

@link(url='https://team-v5ka.testit.software/projects/664/tests/769', name='Проверка открытия меню второго уровня - сабменю framework')
def test_submenu_framework_click_and_open_page(driver):
    main_page_test = MainPage(driver)
    main_page_test.open()
    menu_elements = main_page_test.get_menu_element()
    menu_elements.click_submenu_framework()
    assert driver.current_url == URLs.MAIN_PAGE+subURLs.FRAMEWORK_PAGE, f"Ожидался URL '{URLs.MAIN_PAGE+subURLs.FRAMEWORK_PAGE}, но получен '{driver.get_url()}'"

@link(url='https://team-v5ka.testit.software/projects/664/tests/769', name='Проверка открытия меню второго уровня - сабменю b2b')
def test_submenu_b2b_click_and_open_page(driver):
    main_page_test = MainPage(driver)
    main_page_test.open()
    menu_elements = main_page_test.get_menu_element()
    menu_elements.click_submenu_b2b()
    assert driver.current_url == URLs.MAIN_PAGE+subURLs.B2B_PAGE, f"Ожидался URL '{URLs.MAIN_PAGE+subURLs.B2B_PAGE}, но получен '{driver.get_url()}'"


@link(url='https://team-v5ka.testit.software/projects/664/tests/769', name='Проверка открытия меню второго уровня - сабменю landing')
def test_submenu_landing_click_and_open_page(driver):
    main_page_test = MainPage(driver)
    main_page_test.open()
    menu_elements = main_page_test.get_menu_element()
    menu_elements.click_submenu_landing()
    assert driver.current_url == URLs.MAIN_PAGE+subURLs.LANDING, f"Ожидался URL '{URLs.MAIN_PAGE+subURLs.LANDING}, но получен '{driver.get_url()}'"

