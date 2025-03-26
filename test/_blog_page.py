import allure
import pytest
from allure_commons._allure import feature, link

from pages.blog_page import BlogPage

# тест с мета-тегами вынесен в main_page_test

@feature('Количество элементов в блоке')
def test_blog_page_count_cards_right(driver):
    blog_page_test = BlogPage(driver)
    blog_page_test.open()
    blocks = blog_page_test.get_count_elements()
    blocks.count_cards_assert("block-right", 2)

@feature('Количество элементов в блоке')
def test_blog_page_count_cards_left(driver):
    blog_page_test = BlogPage(driver)
    blog_page_test.open()
    blocks = blog_page_test.get_count_elements()
    blocks.count_cards_assert("block-left", 6)


#проверка карусели на деталке новости
#@allure.feature('Количество элементов в блоке')
#def test_blog_page_count_cards_popular_news(driver):
    #blog_page_test = BlogPage(driver)
    #blog_page_test.open()
    #blog_page_test.close_modal_popup()
    #blocks = blog_page_test.get_count_elements()
    #blocks.count_cards_assert("popular_news", 3)

#объединяем два кейса в один с передачей параметра лево-право
@link(url=' ', name='Открытие страниц блога - левый блок')
@feature('Открытие страниц блога')
@pytest.mark.parametrize("index, side, page_url, page_title, date_blog", [
    ("1", "right", "https://dev.godev.agency/blog/green-it/", "Green IT: Как технологии становятся экологичными", "29.01.2025"),
    ("2", "right", "https://dev.godev.agency/blog/green-it/", "Green IT: Как технологии становятся экологичными", "29.01.2025"),
    ("1", "left", "https://dev.godev.agency/blog/green-it/", "Green IT: Как технологии становятся экологичными", "29.01.2025"),
    ("2", "left", "https://dev.godev.agency/blog/green-it/", "Green IT: Как технологии становятся экологичными", "29.01.2025"),
    ("3", "left", "https://dev.godev.agency/blog/green-it/", "Green IT: Как технологии становятся экологичными", "29.01.2025"),
    ("4", "left", "https://dev.godev.agency/blog/green-it/", "Green IT: Как технологии становятся экологичными", "29.01.2025"),
    ("5", "left", "https://dev.godev.agency/blog/green-it/", "Green IT: Как технологии становятся экологичными", "29.01.2025"),
    ("6", "left", "https://dev.godev.agency/blog/green-it/", "Green IT: Как технологии становятся экологичными", "29.01.2025")
])
def test_blog_page_click_card_block_left_and_data_pages(driver, index, side, page_url, page_title, date_blog):
    blog_page_test = BlogPage(driver)
    blog_page_test.open()
    blog_page_test.click_block_page(index, side, page_url, page_title, date_blog)