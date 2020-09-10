import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from common import is_element_present


class HomePageTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

        cls.driver.get("https://bitwarden.com/")

    def test_cookies(self):
        button = self.driver.find_element_by_css_selector(
            "button.osano-cm-accept-all")
        self.assertTrue(button)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'button.osano-cm-accept-all')))
        element.click()
        self.assertFalse(is_element_present(
            self.driver,
            By.CSS_SELECTOR,
            "button.osano-cm-accept-all")
        )

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
