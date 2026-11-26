from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_to_basket(self):
        self.should_be_button_add_to_basket()
        self.add_product_to_basket()
        self.should_be_prise_in_basket()

    def should_be_button_add_to_basket(self):
        assert self.is_element_present(
            *ProductPageLocators.BUTTON_ADD_TO_BASKET), "Button 'Add to basket' is not found!"

    def add_product_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add_to_basket.click()
        self.solve_quiz_and_get_code()
        assert self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text == self.browser.find_element(
            *ProductPageLocators.TITLE_PRODUCT).text, "The product name does not match"

    def should_be_prise_in_basket(self):
        assert self.browser.find_element(*ProductPageLocators.BASKET_SUM).text == self.browser.find_element(
            *ProductPageLocators.PRICE_PRODUCT).text, "The price does not match"

    def should_not_be_success_message_after_add_product_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Be success message after adding product to basket"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Be success message"

    def should_not_be_success_message_disappeared_after_add_to_basket(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Be success message disappeared after adding product to basket"
