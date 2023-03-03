from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..",".."))
from automation_framework_danacita.base.base_driver import BaseDriver
from automation_framework_danacita.pages.danacita_loginpage import LoginPage
from automation_framework_danacita.utilities.utils import Utils

class HomePage(BaseDriver):
    log =Utils.custom_logger()
    
    def __init__(self, driver):
        super().__init__(driver)
        
    # Locator 
    LOGIN_ICON = "//span[normalize-space()='Masuk']"
    
    def get_login_icon(self):
        return self.wait_until_element_to_be_clickable(By.XPATH, self.LOGIN_ICON)
        
    def click_login_icon(self):
        self.log.info("Click login icon")
        self.get_login_icon().click()
        login_account = LoginPage(self.driver)
        return login_account
