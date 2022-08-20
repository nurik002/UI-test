from selenium.webdriver.common.by import By


class SingUpLocators:
    SING_UP_BUTTON = (By.XPATH, "//div[@class='header-center__right']/button[1]")
    FULL_SING_UP_BUTTON = (By.XPATH, "//div[@class='login-modal-header']/button[2]")

    # form field
    PHONE = (By.XPATH, "//div[2]/div[1]/div[1]/div[1]/input[1]")
    FIRST_NAME = (By.XPATH, "//div[2]/div[1]/div[2]/div[1]/input[1]")
    LAST_NAME = (By.XPATH, "//div[2]/div[1]/div[3]/div[1]/input[1]")
    CHECK_BOX = (By.XPATH, "//label[@class='register-check']/span[1]")
    SUBMIT = (By.XPATH, "//label[@class='register-check']/following-sibling::button")
    CLOSE_BUTTON = (By.XPATH, "//button[@class='modal-close-btn']")


class RegionLocators:
    BUTTON = (By.CSS_SELECTOR, "div[class='header-region'] button")
    ITEMS = (By.CSS_SELECTOR, "div[class='header-region-list'] ul li a")


class FilterLocators:
    # price slider locators
    RIGHT_SLIDE_BUTTON = (By.CSS_SELECTOR, "div[aria-valuetext='933000']")
    LEFT_SLIDE_BUTTON1 = (By.CSS_SELECTOR, "div[aria-valuetext='17000000']")

