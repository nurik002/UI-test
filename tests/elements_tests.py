import time

from pages.base_page import BasePage
from pages.elements_page import SingUp, ChangeRegion, Filter, CheckLinkStatus
from pages.drage_and_drop import DrageDrope


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
                count -= 1

    class TestFilter:
        def test_filter(self, driver):
            filter = Filter(driver, "https://texnomart.uz/kr/katalog/smartfony")
            filter.open()
            # filter.price_slider()
            filter.click_to_show_all_data()

    class TestCheckLink:
        def test_check_link(self, driver):
            link = CheckLinkStatus(driver, 'https://texnomart.uz/kr')
            link.open()
            link, current_link = link.check_link()
            assert link == current_link

        def test_select_option(self, driver):
            link = CheckLinkStatus(driver, 'https://demo.automationtesting.in/Register.html')
            link.open()
            link.select_option()

        def test_upload_file(self, driver):
            # link = CheckLinkStatus(driver, 'https://demo.automationtesting.in/FileUpload.html')
            link = CheckLinkStatus(driver, 'https://tus.io/demo.html')
            link.open()
            link.upload_file()

    class TestDragDrop:
        def test_drag_drop(self, driver):
            drop = DrageDrope(driver, 'https://demo.automationtesting.in/Dynamic.html')
            drop.open()
            drop.drag_drop()
