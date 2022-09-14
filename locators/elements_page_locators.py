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
    ACTIVE_REGION = (By.CSS_SELECTOR, "span[class='region-text text-white-desktop']")


class FilterLocators:
    DOWN = (By.TAG_NAME, 'html')
    # price slider locators
    RIGHT_SLIDE_BUTTON = (By.CSS_SELECTOR, "div[aria-valuetext='933000']")
    LEFT_SLIDE_BUTTON1 = (By.CSS_SELECTOR, "div[aria-valuetext='17000000']")

    # model filter locators
    MODEL_MORE_BUTTON = (
        By.CSS_SELECTOR, "div[class='accordion-item mb-24']:nth-child(3) span[class='f-12 w-bold text']:first-child")
    # ITEMS = (By.CSS_SELECTOR, "div[class='accordion-item mb-24']:nth-child(3) label span")
    ITEMS = (By.CSS_SELECTOR, "div[class='accordion-item mb-24']:nth-child(3) label input")
    PROCESSOR = (By.CSS_SELECTOR, "div[class='accordion-item mb-24']:nth-child(12)")
    PROCESSOR_MORE = (
        By.CSS_SELECTOR, "div[class='accordion-item mb-24']:nth-child(12) span[class='f-12 w-bold text']:first-child")


class CheckLinkLocators:
    LINK = (By.CSS_SELECTOR, "ul[class='header-bottom-list'] li:nth-child(2) a")
    SELECT = (By.XPATH, "//select[@id='Skills']")
    PASS = (By.XPATH, "//input[@ng-model='CPassword']")
    # UPLOAD = (By.XPATH, "//input[@name='input4[]']")
    UPLOAD = (By.XPATH, "//input[@id='js-file-input']")
