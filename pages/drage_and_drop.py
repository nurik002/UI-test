import random
import time

from selenium.webdriver import ActionChains

from locators.drage_drop_locators import DrageDropeLocators
from pages.base_page import BasePage


class DrageDrope(BasePage):
    locators = DrageDropeLocators()

    def drag_drop(self):
        source_element = self.element_is_visible(self.locators.DRAG_AREA)
        target_element = self.element_is_visible(self.locators.DROP_AREA)
        ActionChains(self.driver).drag_and_drop(source_element, target_element).perform()
        time.sleep(1)
