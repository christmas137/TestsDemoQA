import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Elements: Text Box")
class TestTextBoxFeature(BaseTest):

    @allure.title("Change text-box fields")
    @allure.severity("Normal")
    @pytest.mark.usefixtures
    def test_change_text_box_fields(self):
        self.text_box_page.open()
        self.text_box_page.enter_full_name("Egor")
        self.text_box_page.enter_email("germonenko@gmail.com")
        self.text_box_page.enter_current_address("Voronezh")
        self.text_box_page.enter_permanent_address("Voronezh111")
        self.text_box_page.click_submit_button()
        self.text_box_page.is_changes_saved()
        
        
        

    
    
    