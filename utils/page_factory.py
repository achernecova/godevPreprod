from pages.b2b_page import B2BPage
from pages.blog_page import BlogPage
from pages.cms_page import CMSPage
from pages.framework_page import FrameworkPage
from pages.landing_page import LandingPage
from pages.main_page import MainPage
from pages.mobile_dev_page import MobileDevPage
from pages.project_page import ProjectPage
from pages.reviews_page import ReviewsPage
from pages.services_page import ServicesPage
from pages.support_pages import SupportPage
from pages.web_dev_services_page import WebDevServicesPage
from pages.web_develop_page import WebDevelopPage
from pages.web_outstaff_page import WebOutstaffPage


def get_page_instance(page_name, driver):
    page_classes = {
        "main": MainPage,
        "services": ServicesPage,
        "cms": CMSPage,
        "b2b": B2BPage,
        "mobile": MobileDevPage,
        "blog": BlogPage,
        "framework": FrameworkPage,
        "outstaff": WebOutstaffPage,
        "project_page": ProjectPage,
        "reviews": ReviewsPage,
        "support": SupportPage,
        "web_dev_serv": WebDevServicesPage,
        "web_dev": WebDevelopPage,
        "landing": LandingPage
    }
    try:
        return page_classes[page_name](driver)
    except KeyError:
        raise ValueError(f"Неизвестная страница: {page_name}")