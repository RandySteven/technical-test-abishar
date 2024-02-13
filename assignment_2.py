from selenium import webdriver
from selenium.webdriver.common.by import By


class SeleniumAssignment:
    driver = webdriver.Chrome()

    def open_driver(self):
        self.driver.get("https://www.saucedemo.com/")

    def login_user(self):
        user_name = self.driver.find_element(By.ID, "user-name")
        password = self.driver.find_element(By.ID, "password")
        user_name.send_keys("standard_user")
        password.send_keys('secret_sauce')
