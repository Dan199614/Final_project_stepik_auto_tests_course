from .pages.basket_page import BasketPage


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.should_be_basket_link()
    page.should_be_basket_is_empty()
    page.should_be_text_for_basket_is_empty()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/neuromancer_13/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.should_be_basket_link()
    page.should_be_basket_is_empty()
    page.should_be_text_for_basket_is_empty()