# from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..",".."))
from automation_framework_danacita.base.base_driver import BaseDriver
from automation_framework_danacita.utilities.utils import Utils

class LoginPage(BaseDriver):
    log = Utils.custom_logger()
    
    def __init__(self, driver):
        super().__init__(driver)
        
    # Locator
    PHONE_NUMBER_FIELD = "//input[@id='loginMobileInput']"
    PASSWORD_FIELD = "//input[@id='loginPasswordInput']"
    LOGIN_BUTTON = "//div[normalize-space()='Masuk']//div[@id='login-login']"
    ERROR_POPUP_MESSAGE = "//div[@class='css-1rynq56 r-txxmok r-1b43r93 r-135wba7']"
    BACK_BUTTOM = "//div[@class='css-1rynq56 r-lrvibr']"
    
    def get_phone_number_field(self):
        return self.wait_until_element_to_be_clickable(By.XPATH, self.PHONE_NUMBER_FIELD)
    
    def get_password_field(self):
        return self.wait_until_element_to_be_clickable(By.XPATH, self.PASSWORD_FIELD)
    
    def get_login_button(self):
        return self.driver.find_element(By.XPATH, self.LOGIN_BUTTON)
    
    def get_error_popup_message(self):
        error_message = self.wait_until_element_to_be_clickable(By.XPATH, self.ERROR_POPUP_MESSAGE)
        self.log.warning("Pop up error message is " + error_message.text)
        return error_message
    
    def get_back_button(self):
        return self.driver.find_element(By.XPATH, self.BACK_BUTTOM)
        
        
    
    def input_phone_number(self, phone_number):
        self.get_phone_number_field().click()
        self.get_phone_number_field().send_keys(phone_number)
        self.log.info("Typed phone number")
       
    def input_password(self, password): 
        self.get_password_field().click()
        self.get_password_field().send_keys(password)
        self.log.info("Typed password into password field")
        
    def click_login_button(self):
        self.get_login_button().click()
        self.log.info("Click login button")
        
    def click_back_button(self):
        self.get_back_button().click()
        
    def loginToDanacita(self, phone_number, password):
        self.input_phone_number(phone_number)
        self.input_password(password)
        self.click_login_button()
    

