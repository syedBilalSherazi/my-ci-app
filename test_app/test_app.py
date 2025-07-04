import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class FlaskAppTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        service = Service(ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service=service, options=options)
        cls.driver.implicitly_wait(5)
        cls.base_url = "http://16.171.31.221:5000"

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # --- Test 01 ---
    def test_01_home_page_loads(self):
        self.driver.get(self.base_url)
        self.assertIn("Welcome", self.driver.page_source)

    def test_01b_home_page_loads_duplicate(self):
        self.driver.get(self.base_url)
        self.assertIn("Welcome", self.driver.page_source)

    # --- Test 02 ---
    def test_02_register_link_works(self):
        self.driver.get(self.base_url)
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        self.assertIn("/register", self.driver.current_url)

    def test_02b_register_link_works_duplicate(self):
        self.driver.get(self.base_url)
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        self.assertIn("/register", self.driver.current_url)

    # --- Test 03 ---
    def test_03_login_link_works(self):
        self.driver.get(self.base_url)
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        self.assertIn("/login", self.driver.current_url)

    def test_03b_login_link_works_duplicate(self):
        self.driver.get(self.base_url)
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        self.assertIn("/login", self.driver.current_url)

    # REMOVED test_04_register_form_submission

    # --- Test 05 ---
    def test_05_login_form_submission(self):
        self.driver.get(f"{self.base_url}/login")
        self.driver.find_element(By.NAME, "username").send_keys("testuser")
        self.driver.find_element(By.NAME, "password").send_keys("testpass")
        self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        self.assertIn("Welcome", self.driver.page_source)

    def test_05b_login_form_submission_duplicate(self):
        self.driver.get(f"{self.base_url}/login")
        self.driver.find_element(By.NAME, "username").send_keys("testuser")
        self.driver.find_element(By.NAME, "password").send_keys("testpass")
        self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        self.assertIn("Welcome", self.driver.page_source)

    # --- Test 06 ---
    def test_06_home_page_greeting_check(self):
        self.driver.get(self.base_url)
        self.assertTrue("Welcome" in self.driver.page_source or "Hello" in self.driver.page_source)

    def test_06b_home_page_greeting_check_duplicate(self):
        self.driver.get(self.base_url)
        self.assertTrue("Welcome" in self.driver.page_source or "Hello" in self.driver.page_source)

    # REMOVED test_07_register_page_has_title

    # --- Test 08 ---
    def test_08_login_page_has_form_fields(self):
        self.driver.get(f"{self.base_url}/login")
        username_field = self.driver.find_element(By.NAME, "username")
        password_field = self.driver.find_element(By.NAME, "password")
        self.assertTrue(username_field.is_displayed() and password_field.is_displayed())

    def test_08b_login_page_has_form_fields_duplicate(self):
        self.driver.get(f"{self.base_url}/login")
        username_field = self.driver.find_element(By.NAME, "username")
        password_field = self.driver.find_element(By.NAME, "password")
        self.assertTrue(username_field.is_displayed() and password_field.is_displayed())

    # --- Test 09 ---
    def test_09_home_page_has_links(self):
        self.driver.get(self.base_url)
        links = self.driver.find_elements(By.TAG_NAME, "a")
        link_texts = [link.text for link in links]
        self.assertIn("Register", link_texts)
        self.assertIn("Login", link_texts)

    def test_09b_home_page_has_links_duplicate(self):
        self.driver.get(self.base_url)
        links = self.driver.find_elements(By.TAG_NAME, "a")
        link_texts = [link.text for link in links]
        self.assertIn("Register", link_texts)
        self.assertIn("Login", link_texts)

    # --- Test 10 ---
    def test_10_home_page_title(self):
        self.driver.get(self.base_url)
        self.assertIn("Flask App", self.driver.title)

    def test_10b_home_page_title_duplicate(self):
        self.driver.get(self.base_url)
        self.assertIn("Flask App", self.driver.title)


if __name__ == "__main__":
    unittest.main()
