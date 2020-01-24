from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_message_empty_basket(self):
        assert 'Your basket is empty' in self.browser.find_element(*BasketPageLocators.MESSAGE_EMPTY_BASKET).text

    def basket_should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_CONTENT)
