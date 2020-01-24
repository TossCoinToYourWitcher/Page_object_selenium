from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group > a.btn")


class BasketPageLocators:
    MESSAGE_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_CONTENT = (By.CSS_SELECTOR, ".basket_summary")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    PURCHASE_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form.add-to-basket")
    BOOK_NAME_IN_MESSAGE = (By.CSS_SELECTOR, ".alert-success:nth-child(1) div.alertinner strong")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRICE_OF_BOOK = (By.CSS_SELECTOR, ".product_main p")
    PRICE_IN_MESSAGE = (By.CSS_SELECTOR, ".alert.alert-info strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success:nth-child(1)")
