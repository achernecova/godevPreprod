from selenium.webdriver.common.by import By


class Locators:
    click_button_banner = (By.XPATH, "//*[@class='banner']//button")
    button_banner_page = (By.XPATH,"//*[@class='banner has-descr']//button")
    title_page = (By.XPATH, '//h1')
    title_element = (By.XPATH, "//*[@class='section-title half slider-controls']")
    close_modal = (By.XPATH, "//*[@class='close-modal']")
    popup_success = (By.XPATH, "//*[@class='sendmail-popup success']")
    elements_in_card = (By.CLASS_NAME, 'team-card')
    project_type_with_experience = (By.CSS_SELECTOR, '.spec.fs24')
    project_type_not_experience = (By.CSS_SELECTOR, '.spec.fs22')
    date_blog = (By.XPATH, "//*[@class= 'blog-single-banner__date']")
    button_tariff = (By.XPATH, "(//*[@class='service-last-row']//button)[1]")
    team_card = (By.XPATH, "//*[@class='price-frameworks']")
    button_in_card_select_locator = (By.XPATH, "//*[@class='info-card selected']//button")
    #button_in_faq_locator = (By.XPATH, "//*[@class='faq-section']//button")
    button_in_faq_locator = (By.XPATH, "//*[text()='Ask a Question']")
    input_name_locator = (By.XPATH, "//*[@class='request-offer-inputs']//input[@name='name']")
    input_email_locator = (By.XPATH, "//*[@class='request-offer-inputs']//input[@name='email']")
    input_comment_locator = (By.XPATH, "//*[@class='form-textarea']//*[@placeholder='Comment']")
    button_click_locator = (By.XPATH, "//*[@class='request-offer-bottom']//button")
    button_banner_services = (By.XPATH, "//*[@class='banner-button button open-modal']")
    topping_dev_button_locator = (By.XPATH, "//label[@class='topping'][@for='t11']")
    topping_analysts_locator = (By.XPATH, "//label[@class='topping'][@for='t14']")
    button_request = (By.XPATH, "(//button[@class='button outsource-button open-modal'])[1]")
    button_request_outsource_team = (By.XPATH, "(//*[@class='outsource-item']//button)[1]")
    get_text_block = (By.XPATH, "//*[@class='tiles-section']//*[contains(@class, 'section-descr')]")
    get_text_block_type_section = (By.XPATH, "//*[@class='type-section']//*[contains(@class, 'section-descr')]")
    get_title_block = (By.XPATH, "//*[@class='type-section']//h2")
    price_left_title_locator = (By.XPATH, "(//*[@class='price-frameworks__left']//*[@class='price-frameworks__title'])")
    price_left_text_locator =  (By.XPATH, "//*[@class='price-frameworks__left']//*[@class='price-frameworks__text']")
    price_right_title_locator =  (By.XPATH, "//*[@class='price-frameworks__right']//*[@class='price-frameworks__title']")
    price_right_text_locator = (By.XPATH, "//*[@class='price-frameworks__right']//*[@class='price-frameworks__text']")
    section_form_element_locator = (By.XPATH, "//section[@class='section-form']")
    topping_click_locator = (By.XPATH, "//label[@class='topping'][@for='t1']")
    menu_contacts_locator = (By.XPATH, "//*[@class='menu-wrapper']//a[@href= 'https://dev.godev.agency/contacts/']")
    name_input_locator = (By.XPATH, "//*[@class='section-form']//input[@name='name']")
    email_input_locator = (By.XPATH, "//*[@class='section-form']//input[@name='email']")
    message_input_locator = (By.XPATH, "//*[@class='section-form']//*[@name='description']")
    submit_button_locator = (By.XPATH, "//*[@class='section-form']//*[@class='button']")
    button_project_mint_link_locator = (By.XPATH, "//*[@href='https://dev.godev.agency/projects/mint-links/']")
    button_project_sls_locator = (By.XPATH, "//*[@href='https://dev.godev.agency/projects/swift-logistic-solutions/']")
    button_project_find_a_builder_locator = (By.XPATH, "//*[@href='https://dev.godev.agency/projects/find-a-builder/']")
    button_project_vegan_hotel_locator = (By.XPATH, "//*[@href='https://dev.godev.agency/projects/vegan-hotel/']")
    button_project_euro_VPN_locator = (By.XPATH, "//*[@href='https://dev.godev.agency/projects/information-security-service/']")
    button_landing_locator = (By.XPATH, "//*[@href='/services/development-of-a-landing-page/']")
    button_rates_locator = (By.XPATH, "(//a[@class='button open-modal'])[1]")
    title_rates_locator = (By.XPATH, "//h2[@class='section-title max-content']")
    title_convenient_locator = (By.XPATH, "//*[@class='work']//*[@class='section-title max-content']")

    title_convenient_card_locator = (By.XPATH, "//*[@class='work']//*[@class='h3']")

    title_block_app_and_web_development_services_locator = (By.XPATH, "//section[@id='services']//h2")
    text_block_app_and_web_development_services_locator = (By.XPATH, "//section[@id='services']//*[contains(@class, 'section-descr')]")
    title_block_website_dev_locator = (By.XPATH, "//section[@class='advant-section']//h2")
    text_block_website_dev_locator = (By.XPATH, "//section[@class='advant-section']//*[contains(@class, 'section-descr ')]")
    title_block_website_design_locator = (By.XPATH, "//section[@id='projects']//h2")
    text_block_website_design_locator = (By.XPATH, "//section[@id='projects']//*[contains(@class, 'section-descr')]")
    title_block_custom_design_solutions_locator = (By.XPATH, "//*[@class='how-it-staff']//*[@class='section-title half']")
    text_block_custom_design_solutions_locator = (By.XPATH, "//*[@class='how-it-staff']//*[@class='section-descr fs16px half']")
    text_block_it_staff_locator = (By.XPATH, "//*[@class='how-it-staff']//*[@class='section-descr  short']")
    title_block_digital_agency_godev_locator = (By.XPATH, "//section[@class='tiles-section']//*[contains(@class, 'section-title half')]")
    text_block_digital_agency_godev_locator = (By.XPATH, "//section[@class='tiles-section']//*[contains(@class, 'section-descr ')]")
    button_get_in_touch_locator = (By.XPATH, "(//button[@class='get-in-touch-btn open-modal'])[1]")
    block_get_in_touch_locator = (By.XPATH,"(//*[@class='get-in-touch-wrapper'])[1]")

    XPATH_MAP = {
        "blocks": "//*[@class='web-dev-services']",
        "benefits": "//*[@class='advant-card']",
        "how_we_make_web": "//*[contains(@class, 'advant-slider swiper images')]//*[@class='advant-card']",
        "advantages_outsourcing": "//*[@class='advantages-outsourcing__item']",
        "our_proven_web_dev": "//*[contains(@class, 'advant-slider swiper icons ')]//*[@class='advant-card']",
        "why_choose_godev": "//*[@class='advant images']//*[contains(@class, 'advant-card ')]",
        "types_of_it": "//*[@class='types-of-it-card']",
        "what_to_choose": "//*[@class='choise-card']",
        "customer_reviews": "//*[@class='review-card']",
        "web_packages_count": "//*[@class='team-card']",
        "types_of_websites_count_card": "//*[contains(@class, 'tile w-')]",
        "why_godev_outstaff_partner": "//*[@class='tiles-section']//*[contains(@class, 'section-descr')]",
        "advantages_cards_tiles_count": "//*[@class='cards-tiles col-2']//*[@class='card']",
        "carousel_how_make": "//*[contains(@class, 'swiper-slide grabbable ')]",
        "count_card_advantages": "//*[contains(@class, 'swiper-slide grabbable')]",
        "count_card_cooperation_formats": "//*[@class='cooperation-formats-card']",
        "web_dev_services": "//*[@class='card']",
        "swiper_slide": "//*[@class='swiper-slide']",
        "best_web_frameworks": "//*[contains(@class, 'best-frameworks__item ')]",
        "cms_services_cards": "//button[contains(@class, 'card-wrapper')]",
        "back_end_frameworks": "//*[@class='best-frameworks__inner']//*[contains(@class, 'swiper-slide')]",
        "platforms": "//*[@class='card']",
        "adv_item": "//*[@class='adv-item']",
        "block-right": "//*[@class= 'blog__block-right']",
        "block-left": "//*[contains(@class, 'blog__block-left--item')]",
        "popular_news": "//*[contains(@class, 'swiper-slide grabbable ')]"
    }

    @staticmethod
    def get_xpath(project_type):
        if project_type not in Locators.XPATH_MAP:
            raise ValueError("Неверный тип карточки")
        return Locators.XPATH_MAP[project_type]

    @staticmethod
    def get_team_card_more_locator(index):
        return (By.XPATH, f"(//*[@class='team-card']//a[@class='more'])[{index}]")

    @staticmethod
    def get_data_with_attr_and_index_locator(attr, index):
        return (By.XPATH, f"(//*[@class='team-card']//*[@class='{attr}'])[{index + 1}]")

    @staticmethod
    def get_click_block_class_and_index_locator(block_class, index):
        return (By.XPATH, f"(//*[contains(@class, '{block_class}')])[{index}]")

    @staticmethod
    def get_check_packages_data_not_experience_locator(index):
        locator = (By.XPATH, f"//div[contains(@class='team-card')][{index + 1}]")  # Пример
        print(f"Locator returned: {locator}")  # Для отладки
        return locator

    @staticmethod
    def get_project_locator(index):
        return (By.XPATH, f"(//*[@class='projects-title'])[{index}]")

    @staticmethod
    def get_button_more_locator(index):
        return (By.XPATH, f"(//*[contains(@class, 'tile ')]//a[@class='more'])[{index}]")

    @staticmethod
    def check_packages_data_services_title_locator(index):
        return (By.XPATH, f"(//*[@class='card-title'])[1 + {index}]")

    @staticmethod
    def check_packages_data_services_price_locator(index):
        return (By.XPATH, f"(//*[@class='price'])[1 + {index}]")

    @staticmethod
    def get_type_section(tree):
        return tree.xpath("//*[@class='advant-card-content']")

