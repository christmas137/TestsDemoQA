import pytest
from pages.text_box_page import TextBoxPage
from pages.checkbox_page import CheckboxPage
from pages.buttons_page import ButtonsPage


class BaseTest: 
    
    text_box_page: TextBoxPage
    buttons_page: ButtonsPage
    
    @pytest.fixture(autouse=True)
    def setup(self, request, driver): 
        request.cls.driver = driver
        request.cls.text_box_page = TextBoxPage(driver)
        request.cls.buttons_page = ButtonsPage(driver)
        