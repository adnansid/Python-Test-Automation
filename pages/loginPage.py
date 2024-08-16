from selenium.webdriver.common.by import By
from utilities import readConfig

class LoginPage:

    def __init__(self,driver):
        self.driver = driver
    
    def login_credential(self):
        email = readConfig.read_configuration("basic info","email")
        password = readConfig.read_configuration("basic info","password")
        self.driver.find_element(By.ID,"input-email").send_keys(email)
        self.driver.find_element(By.ID,"input-password").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
    
    def login_invalid_credentials(self):
        email = readConfig.read_configuration("basic info","email")
        password = readConfig.read_configuration("basic info","password2")
        self.driver.find_element(By.ID,"input-email").send_keys(email)
        self.driver.find_element(By.ID,"input-password").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
    
    def login_from_excelData(self,email,password):
        self.driver.find_element(By.ID,"input-email").send_keys(email)
        self.driver.find_element(By.ID,"input-password").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
    
    def alert_messeage(self):
        return self.driver.find_element(By.CSS_SELECTOR,".alert").text
