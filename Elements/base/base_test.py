import pytest
from pages.text_box_page import TextBoxPage
from pages.checkbox_page import CheckboxPage


class BaseTest: 
    
    text_box_page: TextBoxPage
    
    @pytest.fixture(autouse=True)
    def setup(self, request, driver): 
        request.cls.driver = driver
        request.cls.text_box_page = TextBoxPage(driver)
        