import pytest
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import time

product_page_link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
main_link = "http://selenium1py.pythonanywhere.com/accounts/login/"


@pytest.mark.parametrize('link', [product_page_link])
@pytest.mark.login
class TestLoginFromProductPage:
    def test_guest_should_see_login_link_on_product_page(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()
        page.go_to_login_page()
        page = LoginPage(browser, browser.current_url)
        page.should_be_login_page()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + "@fakepass"
        login_page = LoginPage(browser, main_link)
        login_page.open()
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    @pytest.mark.parametrize('link', [product_page_link])
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.add_to_cart()
        page.should_be_adding_confirmation()
        page.compare_name()

    @pytest.mark.parametrize('link', [product_page_link])
    def test_user_cant_see_success_message(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()


@pytest.mark.parametrize('link', [product_page_link])
@pytest.mark.xfail(reason="fixing this bug right now")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_cart()
    product_page.should_not_be_success_message()


@pytest.mark.parametrize('link', [product_page_link])
@pytest.mark.xfail(reason="fixing this bug right now")
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_cart()
    product_page.success_message_is_disappeared()


@pytest.mark.parametrize('link', [product_page_link])
@pytest.mark.xfail(reason="negative-check")
def test_message_with_added_product_to_basket(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_cart()
    product_page.go_to_basket_page()
    basket_page = BasketPage(browser, link)
    basket_page.should_be_message_empty_basket()


@pytest.mark.parametrize('link', [product_page_link])
@pytest.mark.xfail(reason="negative-check")
def test_negative_check_for_product_block_with_added_product_to_basket(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_cart()
    product_page.go_to_basket_page()
    basket_page = BasketPage(browser, link)
    basket_page.basket_should_be_empty()


@pytest.mark.parametrize('link', [product_page_link])
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.should_be_adding_confirmation()
    page.compare_name()


@pytest.mark.parametrize('link', [product_page_link])
def test_guest_cant_see_success_message(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.parametrize('link', [product_page_link])
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page = BasketPage(browser, browser.current_url)
    page.basket_should_be_empty()
    page.should_be_message_empty_basket()
