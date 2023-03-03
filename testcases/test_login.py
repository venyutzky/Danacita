from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC
import pytest
import softest
from ddt import ddt, file_data, unpack, data
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..",".."))
from automation_framework_danacita.pages.danacita_homepage import HomePage
from automation_framework_danacita.pages.danacita_loginpage import LoginPage
from automation_framework_danacita.utilities.utils import Utils


@pytest.mark.usefixtures("setup")
@ddt
class TestLogin(softest.TestCase):
    
    log =Utils.custom_logger()
    
    
    # Setup class
    @pytest.fixture(autouse=True)
    def setup_class(self):
        self.in_homepage = HomePage(self.driver)
        self.util = Utils()
        self.in_loginpage = LoginPage(self.driver)
    
    # @data(("081378119248", "Testing123", "Nomor ponsel atau kata sandi salah."), ("081378119299", "Testing123", "Nomor ponsel atau kata sandi salah."))
    @file_data("../testdata/testdata.json")
    @unpack
    def test_login_with_unregistered_account(self, phone_number, password, error_message):
        # Navigate to login page
        self.in_homepage.page_scroll()
        login_account = self.in_homepage.click_login_icon()
        
        # login account to danacita
        login_account.loginToDanacita(phone_number, password)
        
        # Verified the error pop up message
        popup_message = login_account.get_error_popup_message()
        # self.log.warning(popup_message.text)
        self.util.assertErrorMessageText(popup_message, error_message)
        
    

    