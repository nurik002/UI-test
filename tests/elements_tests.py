import time

from pages.base_page import BasePage
from pages.elements_page import SingUp, ChangeRegion, Filter


class TestElements:
    class TestSingUp:
        def test_sing_up(self, driver):
            sing_up = SingUp(driver, "https://texnomart.uz/kr")
            sing_up.open()
            sing_up.open_sing_up()
            sing_up.fill_all_elements()
            time.sleep(3)

    class TestChangeRegion:
        def test_change_region(self, driver):
            region = ChangeRegion(driver, "https://texnomart.uz/kr")
            region.open()
            count = 5
            while count > 0:
                region.click_button()
                region.change_region()
                count -= 1

    class TestFilter:
        def test_filter(self, driver):
            filter = Filter(driver, "https://texnomart.uz/kr/katalog/smartfony")
            filter.open()
            filter.price_slider()
            time.sleep(3)
