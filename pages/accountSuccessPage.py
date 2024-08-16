from selenium.webdriver.common.by import By


class AccountSuccessPage:

    def __init__(self,driver):
        self.driver = driver
    
    def account_success_status(self):
        return self.driver.find_element(By.XPATH,"//div[@id='content']/h1").text  