import random
import time

import requests
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

from locators.elements_page_locators import SingUpLocators, RegionLocators, FilterLocators, CheckLinkLocators
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
        button = self.element_is_visible(self.locators.BUTTON).click()
        list_regions = self.elements_are_visible(self.locators.ITEMS)
        region = list_regions[random.randint(1, 5)]
        ActionChains(self.driver).click(region).perform()

    def check_region(self):
        active_region = self.element_is_present(self.locators.ACTIVE_REGION)
        print(f"ACTIVE = {active_region}")
        return active_region.text


class Filter(BasePage):
    locators = FilterLocators()

    def price_slider(self):
        slider_right_button = self.element_is_visible(self.locators.RIGHT_SLIDE_BUTTON)
        slider_left_button = self.element_is_visible(self.locators.LEFT_SLIDE_BUTTON1)
        ActionChains(self.driver).drag_and_drop_by_offset(slider_right_button, 60, 0).pause(1).perform()
        ActionChains(self.driver).drag_and_drop_by_offset(slider_left_button, -60, 0).perform()

    def click_to_show_all_data(self):
        button = self.element_is_visible(self.locators.PROCESSOR)
        button.click()
        button_more = self.element_is_clickable(self.locators.PROCESSOR_MORE)
        button_more.click()

    def brand_filter(self):
        button = self.elements_are_visible(self.locators.PROCESSOR)
        self.go_to_element(button)
        button.click()

        # ActionChains(self.driver).move_to_element(button_more).click(button_more).perform()


class CheckLinkStatus(BasePage):
    locators = CheckLinkLocators()

    def check_link(self):
        link = self.element_is_visible(self.locators.LINK)
        link_href = link.get_attribute('href')
        request = requests.get(f'{link_href}')
        if request.status_code == 200:
            link.click()
            time.sleep(2)
            url = self.driver.current_url
            return link_href, url
        else:
            return link_href, request.status_code

    def select_option(self):
        select_link = self.element_is_visible(self.locators.SELECT)
        drp = Select(select_link)
        for i in range(10):
            drp.select_by_index(random.randint(1, 18))
            time.sleep(1)

    def upload_file(self):
        upload = self.element_is_visible(self.locators.UPLOAD)
        self.go_to_element(upload)
        time.sleep(2)
        upload.send_keys(r"C:\Users\User\Desktop\git.txt")
        time.sleep(5)
