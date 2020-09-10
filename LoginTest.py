import os
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from common import is_element_present

WAIT_TIMEOUT = 5


class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(WAIT_TIMEOUT)
        cls.driver.maximize_window()

        cls.driver.get("https://vault.bitwarden.com/#/")

    def test_aa_fill_login_form(self):
        email = self.driver.find_element_by_name("Email")
        email.send_keys("n.e.riviere@gmail.com")
        password = self.driver.find_element_by_name("MasterPassword")
        password.send_keys(os.environ["MASTER_PASSWORD"])
        password.submit()

    def test_ab_check_vault_access(self):
        self.assertTrue(is_element_present(self.driver, By.TAG_NAME, "h1"))
        title = self.driver.find_element_by_tag_name("h1").text
        self.assertEqual(title, "Mon coffre")

    def test_ac_add_new_element(self):
        add_new = self.driver.find_element_by_xpath(
            '//button[contains(., "Ajouter un élément")]'
        )
        add_new.click()
        modal_title = self.driver.find_element_by_id("cipherAddEditTitle")
        self.assertEqual(modal_title.text, "AJOUTER UN ÉLÉMENT")

    def test_ad_fill_new_element(self):
        name = self.driver.find_element_by_name("Name")
        name.send_keys("Test")
        username = self.driver.find_element_by_name("Login.Username")
        username.send_keys("John")
        password = self.driver.find_element_by_name("Login.Password")
        password.send_keys("Doe")
        uri = self.driver.find_element_by_id("loginUri0")
        uri.send_keys("http://www.google.com")
        uri.submit()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
