from datetime import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from pages.accountSuccessPage import AccountSuccessPage
from pages.homePage import HomePage
from pages.registrationPage import RegistrationPage

@pytest.mark.usefixtures("setup_and_teardown")
class TestRegister:

    def test_login_valid_credential(self):
        home_page = HomePage(self.driver)
        home_page.select_login_or_registration_option("Register")
        registration = RegistrationPage(self.driver)
        registration.first_Name("klaus")
        registration.last_Name("rolf")
        registration.email(self.genrate_email())
        registration.telephone("1234566788")
        registration.input_password("12345")
        registration.confirm_password("12345")
        registration.checkbox()
        registration.submit()
        account_Success_Page = AccountSuccessPage(self.driver)
        assert account_Success_Page.account_success_status().__contains__("Your Account Has Been Created!")
        

    def test_with_duplicate_email(self):
        home_page = HomePage(self.driver)
        home_page.select_login_or_registration_option("Register")
        registration = RegistrationPage(self.driver)
        registration.first_Name("klaus")
        registration.last_Name("rolf")
        registration.email("amotooricap9@gmail.com")
        registration.telephone("1234566788")
        registration.input_password("12345")
        registration.confirm_password("12345")
        registration.checkbox()
        registration.submit()
        assert registration.warning_status().__contains__("Warning: E-Mail Address is already registered!")
       

    def genrate_email(self):
        time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "eddi" +time_stamp+"@gmail.com"
