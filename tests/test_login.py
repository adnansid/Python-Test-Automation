import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pages.accountPage import AccountPage
from pages.homePage import HomePage
from pages.loginPage import LoginPage
from utilities import excelRead

@pytest.mark.usefixtures("setup_and_teardown")

class TestLogin:
        
    def test_login_valid_credential(self):
      home_page = HomePage(self.driver)
      home_page.select_login_or_registration_option("Login")
      time.sleep(1)
      login_page = LoginPage(self.driver)
      login_page.login_credential()
      account_Page = AccountPage(self.driver)
      assert  account_Page.login_status_verify()

    @pytest.mark.parametrize("email_address , password",excelRead.get_data_from_excel("resources/username.xlsx","loginData"))
    def test_login_credential_from_excelFile(self,email_address,password):
      home_page = HomePage(self.driver)
      home_page.select_login_or_registration_option("Login")
      time.sleep(1)
      login_page = LoginPage(self.driver)
      login_page.login_from_excelData(email_address,password)
      account_Page = AccountPage(self.driver)
      assert  account_Page.login_status_verify()


    def test_login_invalid_credential(self):
      home_page = HomePage(self.driver)
      home_page.select_login_or_registration_option("Login")
      login_page = LoginPage(self.driver)
      login_page.login_invalid_credentials()
      assert login_page.alert_messeage().__contains__("Warning: No match for E-Mail Address and/or Password.")
       
      
