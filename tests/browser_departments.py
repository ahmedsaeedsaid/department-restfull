# tests/test_selenium.py
import time
import unittest
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# You can use chromedriver-autoinstaller to automatically manage the driver
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()  # Installs ChromeDriver automatically if needed

class TestDjangoApp(StaticLiveServerTestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)  # wait for elements to be present
        self.username = 'PERSON123'
        self.password = 'PASS@123'
        self.email = 'testuser@example.com'

    def tearDown(self):
        self.driver.quit()

    def test_01_register_user(self):
        # Navigate to the registration page
        self.driver.get(f'{self.live_server_url}/register/')

        # Find form elements and input data
        self.driver.find_element(By.NAME, 'username').send_keys(self.username)
        self.driver.find_element(By.NAME, 'email').send_keys(self.email)
        self.driver.find_element(By.NAME, 'password1').send_keys(self.password)
        self.driver.find_element(By.NAME, 'password2').send_keys(self.password)

        # Submit the form
        self.driver.find_element(By.CSS_SELECTOR, 'button').click()

        # Wait for the response and check for success
        time.sleep(2)
        self.assertIn("Login", self.driver.page_source)

    def test_02_login_user(self):

        self.test_01_register_user()
        # Assuming the user is already created or manually inserted into the database for testing
        self.driver.get(f'{self.live_server_url}/login/')

        self.driver.find_element(By.NAME, 'username').send_keys(self.username)
        self.driver.find_element(By.NAME, 'password').send_keys(self.password)
        self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

        # Check that the user is redirected to a page that confirms login success
        time.sleep(2)
        self.assertIn("Welcome", self.driver.page_source)

    def test_03_create_department(self):
        # First log in as the test user
        self.test_02_login_user()

        # Navigate to the "Create Department" page
        self.driver.get(f'{self.live_server_url}/create/')

        # Fill out the form to create a new department
        self.driver.find_element(By.NAME, 'name').send_keys('IT Department')

        # Submit the form
        self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

        # Check if the department was successfully created
        time.sleep(2)
        self.assertIn('Welcome', self.driver.page_source)

    def test_04_update_department(self):
        # First log in
        self.test_02_login_user()

        # Create a department for testing
        self.test_03_create_department()

        self.driver.get(f'{self.live_server_url}/')

        self.driver.find_element(By.LINK_TEXT, 'Edit').click()

        # Update the department name
        self.driver.find_element(By.NAME, 'name').clear()
        self.driver.find_element(By.NAME, 'name').send_keys('HR Department')

        # Submit the form
        self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

        # Verify that the department was updated
        time.sleep(2)
        self.assertIn('Welcome', self.driver.page_source)

    def test_05_delete_department(self):
        # First log in
        self.test_02_login_user()

        # Create a department for testing
        self.test_03_create_department()

        # Navigate to the department list page
        self.driver.get(f'{self.live_server_url}/')

        self.driver.find_element(By.LINK_TEXT, 'Delete').click()


        # Click the delete button (assuming the department ID is 1)
        self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()


        # Verify that the department was deleted
        time.sleep(2)
        self.assertNotIn('IT Department', self.driver.page_source)

if __name__ == '__main__':
    unittest.main()
