from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group > a.btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    MESSAGE_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_CONTENT = (By.CSS_SELECTOR, ".basket_summary")


class LoginPageLocators(object):
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    PASS_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    REPEAT_PASS_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_SUBMIT_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")


class ProductPageLocators:
    PURCHASE_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form.add-to-basket")
    BOOK_NAME_IN_MESSAGE = (By.CSS_SELECTOR, ".alert-success:nth-child(1) div.alertinner strong")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRICE_OF_BOOK = (By.CSS_SELECTOR, ".product_main p")
    PRICE_IN_MESSAGE = (By.CSS_SELECTOR, ".alert.alert-info strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success:nth-child(1)")
