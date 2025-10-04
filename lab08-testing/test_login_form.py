import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestLoginForm(unittest.TestCase):

    def setUp(self):
        # Khởi tạo ChromeDriver
        self.driver = webdriver.Chrome()
        # Mở file login.html (chỉnh đường dẫn theo máy bạn)
        self.driver.get("file:///C:/Users/Nam/Desktop/login.html")
        self.driver.maximize_window()

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

    def test_empty_fields(self):
        driver = self.driver
        # Nhấn login khi chưa nhập gì
        driver.find_element(By.CLASS_NAME, "login-btn").click()
        alert = driver.switch_to.alert
        self.assertEqual(alert.text, "Vui lòng nhập Username và Password!")
        alert.accept()

    def test_invalid_login(self):
        driver = self.driver
        driver.find_element(By.ID, "username").send_keys("user")
        driver.find_element(By.ID, "password").send_keys("wrong")
        driver.find_element(By.CLASS_NAME, "login-btn").click()

        alert = driver.switch_to.alert
        self.assertEqual(alert.text, "Sai Username hoặc Password!")
        alert.accept()

    def test_valid_login(self):
        driver = self.driver
        driver.find_element(By.ID, "username").send_keys("admin")
        driver.find_element(By.ID, "password").send_keys("123")
        driver.find_element(By.CLASS_NAME, "login-btn").click()

        alert = driver.switch_to.alert
        self.assertEqual(alert.text, "Đăng nhập thành công!")
        alert.accept()

    def test_cancel_button(self):
        driver = self.driver
        driver.find_element(By.ID, "username").send_keys("someuser")
        driver.find_element(By.ID, "password").send_keys("somepass")
        driver.find_element(By.ID, "remember").click()

        driver.find_element(By.CLASS_NAME, "cancel-btn").click()

        # Kiểm tra reset form
        self.assertEqual(driver.find_element(By.ID, "username").get_attribute("value"), "")
        self.assertEqual(driver.find_element(By.ID, "password").get_attribute("value"), "")
        self.assertFalse(driver.find_element(By.ID, "remember").is_selected())

if __name__ == "__main__":
    unittest.main()
