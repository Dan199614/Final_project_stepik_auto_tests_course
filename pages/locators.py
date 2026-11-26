from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "a[href*='login']")
    BASKET_LINK = (By.CSS_SELECTOR, "a[href*='basket']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "a[href*='login']")



class LoginPageLocators:
    LOGIN_INPUT = (By.CSS_SELECTOR, "#id_login-username")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[name='login_submit']")

    REGISTRATION_LOGIN_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD_RETRY_INPUT = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert strong")
    TITLE_PRODUCT = (By.CSS_SELECTOR, ".product_main h1")
    BASKET_SUM = (By.CSS_SELECTOR, ".alert:last-child strong")
    PRICE_PRODUCT = (By.CSS_SELECTOR, "p.price_color")

class BasketPageLocators:
    BASKET_TITLE = (By.CSS_SELECTOR, ".basket-title")
    BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner p")