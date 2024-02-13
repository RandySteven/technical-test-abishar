from selenium import webdriver
from selenium.webdriver.common.by import By


class SeleniumAssignment:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def open_driver(self):
        self.driver.get("https://www.saucedemo.com/")

    def login_user(self):
        user_name = self.driver.find_element(By.ID, "user-name")
        password_field = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.ID, "login-button")

        user_name.send_keys(user_name)
        password_field.send_keys(password_field)
        login_button.click()

    def add_items_to_cart(self):
        inventory_items = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        for item in inventory_items:
            add_to_cart_button = item.find_element(By.CLASS_NAME, "btn_inventory")
            add_to_cart_button.click()

    def proceed_to_checkout(self):
        cart_icon = self.driver.find_element(By.CLASS_NAME, "shopping_cart_container")
        cart_icon.click()
        checkout_button = self.driver.find_element(By.CSS_SELECTOR, ".checkout_button")
        checkout_button.click()

