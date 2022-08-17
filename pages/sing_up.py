from locators.sing_up_locators import SingUpLocators
from pages.base_page import BasePage


class SingUp(BasePage):
    locators = SingUpLocators()

    def fill_all_elements(self):
        self.element_is_visible(self.locators.PHONE).send_keys('9-555-8899')
        self.element_is_visible(self.locators.FIRST_NAME).send_keys('Asal')
        self.element_is_visible(self.locators.LAST_NAME).send_keys('Normatova')
