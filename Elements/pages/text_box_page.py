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
        self.name = full_name
        
    def enter_email(self, email):
        self.wait.until(EC.element_to_be_clickable(self.EMAIL_FIELD)).send_keys(email)
        self.email = email
    
    def enter_current_address(self, current_address):
        self.wait.until(EC.element_to_be_clickable(self.CURRENT_ADDRESS_FIELD)).send_keys(current_address)
        self.current_address = current_address
    
    def enter_permanent_address(self, permanent_address):
        self.wait.until(EC.element_to_be_clickable(self.PERMANENT_ADRESS_FIELD)).send_keys(permanent_address)
        self.permanent_address = permanent_address
        
    def click_submit_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()
        
    def is_changes_saved(self):
        self.wait.until(EC.text_to_be_present_in_element_value(self.FULL_NAME_FIELD, self.name))
        self.wait.until(EC.text_to_be_present_in_element_value(self.EMAIL_FIELD, self.email))
        self.wait.until(EC.text_to_be_present_in_element_value(self.CURRENT_ADDRESS_FIELD, self.current_address))
        self.wait.until(EC.text_to_be_present_in_element_value(self.PERMANENT_ADRESS_FIELD,self.permanent_address))
    

