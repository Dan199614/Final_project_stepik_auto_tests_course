from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")

class LoginPageLocators:
    LOGIN_INPUT = (By.CSS_SELECTOR, "#id_login-username")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[name='login_submit']")
    REGISTRATION_LOGIN_INPUT = (By.CSS_SELECTOR, "#registration-email")
    REGISTRATION_PASSWORD_INPUT = (By.CSS_SELECTOR, "id_registration-password1")
    REGISTRATION_PASSWORD_RETRY_INPUT = (By.CSS_SELECTOR, "id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")
