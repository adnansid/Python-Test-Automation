from selenium.webdriver.common.by import By



class AccountPage:

    def __init__(self,driver):
        self.driver = driver
    
    def login_status_verify(self):
        return self.driver.find_element(By.LINK_TEXT,"Edit your account information").is_displayed  