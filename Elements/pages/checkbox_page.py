from base.base_page import BasePage
from config.links import ElemetLinks
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class CheckboxPage(BasePage):
    
    PAGE_URL = ElemetLinks.CHECKBOX_PAGE
    EXPAND_BUTTON = ("xpath", "//button[@title='Expand all']")
    # Локаторы для чекбоксов
    CHECKBOX_COMMANDS = (By.ID, "tree-node-commands")
    CHECKBOX_REACT = (By.ID, "tree-node-react")
    CHECKBOX_PRIVATE = (By.ID, "tree-node-private")
    CHECKBOX_EXCELFILE = (By.ID, "tree-node-excelFile")

    # Локаторы для лейблов чекбоксов (для клика)
    LABEL_COMMANDS = (By.CSS_SELECTOR, "label[for='tree-node-commands']")
    LABEL_REACT = (By.CSS_SELECTOR, "label[for='tree-node-react']")
    LABEL_PRIVATE = (By.CSS_SELECTOR, "label[for='tree-node-private']")
    LABEL_EXCELFILE = (By.CSS_SELECTOR, "label[for='tree-node-excelFile']")

    def click_expand_button(self):
        self.wait.until(EC.element_to_be_clickable(self.EXPAND_BUTTON)).click()
    
    def click_checkbox(self, label_locator):
        self.wait.until(EC.element_to_be_clickable(label_locator)).click()

    def is_checkbox_checked(self, checkbox_locator):
        checkbox_icon = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, f"label[for='{checkbox_locator[1]}'] span.rct-checkbox > svg")))
        return "rct-icon-check" in checkbox_icon.get_attribute("class")

    def click_commands_checkbox(self):
        self.click_checkbox(self.LABEL_COMMANDS)
        
    def click_react_checkbox(self):
        self.click_checkbox(self.LABEL_REACT)
        
    def click_private_checkbox(self):
        self.click_checkbox(self.LABEL_PRIVATE)
        
    def click_excelfile_checkbox(self):
        self.click_checkbox(self.LABEL_EXCELFILE)

    def is_commands_checkbox_checked(self):
        return self.is_checkbox_checked(self.CHECKBOX_COMMANDS)
        
    def is_react_checkbox_checked(self):
        return self.is_checkbox_checked(self.CHECKBOX_REACT)
        
    def is_private_checkbox_checked(self):
        return self.is_checkbox_checked(self.CHECKBOX_PRIVATE)
        
    def is_excelfile_checkbox_checked(self):
        return self.is_checkbox_checked(self.CHECKBOX_EXCELFILE)