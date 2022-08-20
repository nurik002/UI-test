import random
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from locators.elements_page_locators import SingUpLocators, RegionLocators, FilterLocators
from pages.base_page import BasePage


class SingUp(BasePage):
    locators = SingUpLocators()

    def open_sing_up(self):
        self.element_is_visible(self.locators.SING_UP_BUTTON).click()
        self.element_is_visible(self.locators.FULL_SING_UP_BUTTON).click()

    def fill_all_elements(self):
        self.element_is_visible(self.locators.PHONE).send_keys('94-555-8899')
        self.element_is_visible(self.locators.FIRST_NAME).send_keys('Asal')
        self.element_is_visible(self.locators.LAST_NAME).send_keys('Normatova')
        self.element_is_visible(self.locators.CHECK_BOX).click()
        self.element_is_visible(self.locators.SUBMIT).click()
        self.element_is_visible(self.locators.CLOSE_BUTTON).click()


class ChangeRegion(BasePage):
    locators = RegionLocators()

    def click_button(self):
        self.element_is_visible(self.locators.BUTTON).click()

    def change_region(self):
        item_list = self.elements_are_visible(self.locators.ITEMS)

        item = item_list[random.randint(1, 7)]
        self.click_button()
        item.click()


class Filter(BasePage):
    locators = FilterLocators()

    def price_slider(self):
        slider_right_button = self.element_is_visible(self.locators.RIGHT_SLIDE_BUTTON)
        slider_left_button = self.element_is_visible(self.locators.LEFT_SLIDE_BUTTON1)
        ActionChains(self.driver).drag_and_drop_by_offset(slider_right_button, 60, 0).pause(1).perform()
        ActionChains(self.driver).drag_and_drop_by_offset(slider_left_button, -60, 0).perform()
