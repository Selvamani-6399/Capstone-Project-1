import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
from time import sleep


class OrangeHRM(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)
        self.url = "https://opensource-demo.orangehrmlive.com"

    def tearDown(self):
        self.driver.quit()

    def test_successful_employee_login(self):

        try:
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.driver.find_element(By.NAME, "username").send_keys("Admin")
            self.driver.find_element(By.NAME, "password").send_keys("admin123")
            self.driver.find_element(
                By.XPATH, "//button[@type='submit']").click()
            time.sleep(5)

            expectedurl = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
            curenturl = self.driver.current_url
            if (curenturl == expectedurl):

                print("login successfully")
            else:
                print("Invalid credentials")
        except Exception as e:
            print(f"Exception occurred: {e}")

    def test_invalid_employee_login(self):

        try:
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.driver.find_element(By.NAME, "username").send_keys("Admin")
            self.driver.find_element(
                By.NAME, "password").send_keys("invalid login")
            self.driver.find_element(
                By.XPATH, "//button[@type='submit']").click()
            time.sleep(5)

            if self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p').is_displayed():
                print("Invalid credentials")

            else:
                print("Login successfully")
        except Exception as e:
            print(f"Exception occurred: {e}")

    def test_add_new_employee(self):
        try:
            # Log in as Admin
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.driver.find_element(By.NAME, "username").send_keys("Admin")
            self.driver.find_element(By.NAME, "password").send_keys("admin123")
            self.driver.find_element(
                By.XPATH, "//button[@type='submit']").click()
            time.sleep(5)

            # Add a new employee in the PIM module
            self.driver.find_element(
                By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span').click()
            time.sleep(5)
            self.driver.find_element(
                By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button').click()
            time.sleep(10)
            self.driver.find_element(By.NAME, "firstName").send_keys("Selva")
            self.driver.find_element(By.NAME, "lastName").send_keys("Mani")
            self.driver.find_element(
                By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]').click()
            time.sleep((0.5))

            # To validate the success massage displayed on the webpage
            success_message = self.driver.find_element(
                By.XPATH, '//*[@id="app"]/div[2]/div/div[1]/div[2]/p[2]').text
            print(f"Popup message: {success_message}")
        except Exception as e:
            print(f"Exception occurred: {e}")

    def test_edit_new_employee(self):
        try:
            # Log in as Admin
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.driver.find_element(By.NAME, "username").send_keys("Admin")
            self.driver.find_element(By.NAME, "password").send_keys("admin123")
            self.driver.find_element(
                By.XPATH, "//button[@type='submit']").click()
            time.sleep(5)

            # edit a employee detail in the PIM module
            self.driver.find_element(
                By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span').click()
            self.driver.maximize_window()
            time.sleep(5)

            self.driver.find_element(
                By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[9]/div/button[2]').click()
            time.sleep(10)
            self.driver.find_element(By.NAME, "firstName").send_keys("Selva")
            self.driver.find_element(By.NAME, "lastName").send_keys("lastName")
            self.driver.find_element(
                By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button').click()
            time.sleep((0.5))

            # To validate the success massage displayed on the webpage
            success_message = self.driver.find_element(
                By.XPATH, '//*[@id="app"]/div[2]/div/div[1]/div[2]/p[2]').text
            print(f"Popup message: {success_message}")
        except Exception as e:
            print(f"Exception occurred: {e}")

    def test_delete_employee(self):
        try:
            # Log in as Admin
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.driver.find_element(By.NAME, "username").send_keys("Admin")
            self.driver.find_element(By.NAME, "password").send_keys("admin123")
            self.driver.find_element(
                By.XPATH, "//button[@type='submit']").click()
            time.sleep(5)

            # Add a delete employee in the PIM module
            self.driver.find_element(
                By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span').click()
            time.sleep(5)

            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[9]/div/button[1]').click()
            time.sleep(5)
            self.driver.find_element(
                By.XPATH, '//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]').click()
            time.sleep((0.5))

            # To validate the success massage displayed on the webpage
            success_message = self.driver.find_element(
                By.XPATH, '//*[@id="app"]/div[2]/div/div[1]/div[2]/p[2]').text
            print(f"Popup message: {success_message}")
            time.sleep(5)
        except Exception as e:
            print(f"Exception occurred: {e}")


if __name__ == "__main__":
    unittest.main()