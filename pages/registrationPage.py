from selenium.webdriver.common.by import By

class RegistrationPage:

    def __init__(self,driver):
        self.driver = driver
    
    def first_Name(self,firstName):
        self.driver.find_element(By.ID,"input-firstname").send_keys(firstName)
    def last_Name(self,lastName):
        self.driver.find_element(By.ID,"input-lastname").send_keys(lastName)
    def email(self,email):
        self.driver.find_element(By.ID,"input-email").send_keys(email)
    def telephone(self,telephone_number):
        self.driver.find_element(By.ID,"input-telephone").send_keys(telephone_number)    
    def input_password(self,password):
        self.driver.find_element(By.ID,"input-password").send_keys(password)
    def confirm_password(self,confirm_password):
        self.driver.find_element(By.ID,"input-confirm").send_keys(confirm_password)
    def checkbox(self):
        self.driver.find_element(By.NAME,"agree").click()
    def submit(self):
        self.driver.find_element(By.CSS_SELECTOR,"input.btn").click()
    
    def warning_status(self):
        return self.driver.find_element(By.XPATH,"//div[@id='account-register']/div[1]").text 