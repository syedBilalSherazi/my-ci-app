import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class FlaskAppTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        cls.driver = webdriver.Chrome(options=options)
        cls.driver.implicitly_wait(5)
        cls.base_url = "http://127.0.0.1:5000"

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_01_home_page_loads(self):
        self.driver.get(self.base_url)
        self.assertIn("Welcome", self.driver.page_source)

    def test_02_register_link_works(self):
        self.driver.get(self.base_url)
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        self.assertIn("/register", self.driver.current_url)

    def test_03_login_link_works(self):
        self.driver.get(self.base_url)
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        self.assertIn("/login", self.driver.current_url)

    def test_04_register_form_submission(self):
        self.driver.get(f"{self.base_url}/register")
        self.driver.find_element(By.NAME, "username").send_keys("testuser")
        self.driver.find_element(By.NAME, "password").send_keys("testpass")
        self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        self.assertIn("Welcome", self.driver.page_source)

    def test_05_login_form_submission(self):
        self.driver.get(f"{self.base_url}/login")
        self.driver.find_element(By.NAME, "username").send_keys("testuser")
        self.driver.find_element(By.NAME, "password").send_keys("testpass")
        self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        self.assertIn("Welcome", self.driver.page_source)

    def test_06_register_validation(self):
        self.driver.get(f"{self.base_url}/register")
        self.driver.find_element(By.NAME, "username").send_keys("")
        self.driver.find_element(By.NAME, "password").send_keys("")
        self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        self.assertIn("Username and password required", self.driver.page_source)

    def test_07_login_invalid_user(self):
        self.driver.get(f"{self.base_url}/login")
        self.driver.find_element(By.NAME, "username").send_keys("wronguser")
        self.driver.find_element(By.NAME, "password").send_keys("wrongpass")
        self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        self.assertIn("Invalid username or password", self.driver.page_source)

    def test_08_back_to_home_from_register(self):
        self.driver.get(f"{self.base_url}/register")
        self.driver.back()
        self.assertIn("Welcome", self.driver.page_source)

    def test_09_home_page_has_links(self):
        self.driver.get(self.base_url)
        links = self.driver.find_elements(By.TAG_NAME, "a")
        link_texts = [link.text for link in links]
        self.assertIn("Register", link_texts)
        self.assertIn("Login", link_texts)

    def test_10_home_page_title(self):
        self.driver.get(self.base_url)
        self.assertIn("Flask App", self.driver.title)

if __name__ == "__main__":
    unittest.main()
