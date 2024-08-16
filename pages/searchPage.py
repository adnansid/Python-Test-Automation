from selenium.webdriver.common.by import By

class SearchPage:

    def __init__(self,driver):
        self.driver = driver
    
    def display_status_verify(self):
        return self.driver.find_element(By.LINK_TEXT, "HP LP3065").is_displayed

    def retrieve_no_product_found(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#content > p:nth-child(7)").text