from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_link(self):
        assert "basket" in self.browser.current_url, "URL basket is not correct!"

    def should_be_basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_TITLE), "Basket is not empty!"

    def should_be_text_for_basket_is_empty(self):
        assert "Your basket is empty." in self.browser.find_element(*BasketPageLocators.BASKET_TEXT).text, "Basket is not empty! Text is not correct!"