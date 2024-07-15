import allure
from base.base_page import BasePage
from config.links import ElemetLinks
from selenium.webdriver.support import expected_conditions as EC


class ButtonsPage(BasePage):
    
    PAGE_URL = ElemetLinks.BUTTONS_PAGE
    
    DOUBLE_CLICK_BUTTON = ("xpath", "//button[@id='doubleClickBtn']")
    RIGHT_CLICK_BUTTON = ("xpath", "//button[@id='rightClickBtn']")
    CLICK_ME_BUTTON = ("xpath", "//button[text()='Click Me']")
    
    @allure.step("Double-click on the button")
    def click_to_double_button (self):
        double_click_btn = self.wait.until(EC.element_to_be_clickable(self.DOUBLE_CLICK_BUTTON))
        self.action.double_click(double_click_btn).perform()
        
    @allure.step("Right-click on the button")    
    def click_to_right_button (self):
        right_click_button = self.wait.until(EC.element_to_be_clickable(self.RIGHT_CLICK_BUTTON))
        self.action.context_click(right_click_button).perform()
        
    @allure.step("Left-click on the button")
    def click_to_click_me_botton(self):
        self.wait.until(EC.element_to_be_clickable(self.CLICK_ME_BUTTON)).click()
        
    