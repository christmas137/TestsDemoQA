from base.base_page import BasePage
from config.links import ElemetLinks
from selenium.webdriver.support import expected_conditions as EC

class TextBoxPage(BasePage):
    
    PAGE_URL = ElemetLinks.TEXT_BOX_PAGE
    
    FULL_NAME_FIELD = ("xpath", "//input[@id='userName']")
    EMAIL_FIELD = ("xpath","//input[@id='userEmail']")
    CURRENT_ADDRESS_FIELD = ("xpath", "//textarea[@id='currentAddress']")
    PERMANENT_ADRESS_FIELD = ("xpath", "//textarea[@id='permanentAddress']")
    SUBMIT_BUTTON = ("xpath", "//button[@id='submit']")
    
    def enter_full_name(self, full_name):
        self.wait.until(EC.element_to_be_clickable(self.FULL_NAME_FIELD)).send_keys(full_name)
        
    def enter_email(self, email):
        self.wait.until(EC.element_to_be_clickable(self.EMAIL_FIELD)).send_keys(email)
    
    def enter_current_address(self, current_address):
        self.wait.until(EC.element_to_be_clickable(self.CURRENT_ADDRESS_FIELD)).send_keys(current_address)
    
    def enter_permanent_address(self, permanent_address):
        self.wait.until(EC.element_to_be_clickable(self.PERMANENT_ADRESS_FIELD)).send_keys(permanent_address)
        
    def click_submit_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()
        
        
    

