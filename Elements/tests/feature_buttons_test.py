import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Elements: Buttons")
class TestButtonsFeature(BaseTest):

    @allure.title("Сlickability check buttons")
    @allure.severity("Normal")
    @pytest.mark.usefixtures
    def test_click_to_all_buttons(self):
        self.buttons_page.open()
        self.buttons_page.click_to_double_button()
        self.buttons_page.click_to_right_button()
        self.buttons_page.click_to_click_me_botton()
        self.buttons_page.make_screen("Scr")