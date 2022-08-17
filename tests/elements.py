import time

from pages.base_page import BasePage
from pages.sing_up import SingUp


class TestElements:
    class TestSingUp:
        def test_sing_up(self, driver):
            sing_up = SingUp(driver, 'https://texnomart.uz/kr')
            sing_up.open()
            sing_up.fill_all_elements()
            time.sleep(3)



