from selenium.webdriver.common.by import By



class HomePage:

    def __init__(self,driver):
        self.driver = driver
    
    def enter_product_into_searchbox(self,productName):
        self.driver.find_element(By.NAME, "search").send_keys(productName)
        self.driver.find_element(By.CSS_SELECTOR, ".btn-default").click()
    
    def select_login_or_registration_option(self,option):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, option).click()