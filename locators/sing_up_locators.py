from selenium.webdriver.common.by import By


class SingUpLocators:
    SING_UP_BUTTON = (By.XPATH, "//div[@class='header-center__right']/button[1]")
    FULL_SING_UP_BUTTON = (By.XPATH, "//div[@class='login-modal-header']/button[2]")

    # form field
    PHONE = (By.XPATH, "//div[@class='login-modal-content']/div[2]//div[@class='form-item'][1]")
    FIRST_NAME = (By.XPATH, "//div[@class='login-modal-content']/div[2]//div[@class='form-item'][2]")
    LAST_NAME = (By.XPATH, "//div[@class='login-modal-content']/div[2]//div[@class='form-item'][2]")
