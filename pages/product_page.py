import math

from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException


class ProductPage(BasePage):
    def add_to_cart(self):
        button = self.browser.find_element(*ProductPageLocators.PURCHASE_BUTTON)
        button.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_adding_confirmation(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not present"

    def compare_price(self):
        price_in_message = self.browser.find_element(*ProductPageLocators.PRICE_IN_MESSAGE).text
        price_on_page = self.browser.find_element(*ProductPageLocators.PRICE_OF_BOOK).text
        assert price_in_message == price_on_page, "Price not equal"

    def compare_name(self):
        name_in_message = self.browser.find_element(*ProductPageLocators.BOOK_NAME_IN_MESSAGE).text
        name_on_page = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        assert name_in_message == name_on_page, "Names not equal"
