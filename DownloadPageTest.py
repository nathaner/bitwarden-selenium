import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from common import is_element_present

WAIT_TIMEOUT = 5


class HomePageTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(WAIT_TIMEOUT)
        cls.driver.maximize_window()

        cls.driver.get("https://bitwarden.com/")

    def test_aa_go_to_download_page(self):
        link = self.driver.find_element_by_link_text("Download")
        link.click()

    def test_ab_desktop_links(self):
        platforms = ["a.windows", "a.macos", "a.linux"]

        for platform in platforms:
            self.assertTrue(is_element_present(
                self.driver,
                By.CSS_SELECTOR,
                platform)
            )

    def test_ac_browser_links(self):
        browsers = [
            "a.chrome",
            "a.firefox",
            "a.opera",
            "a.edge",
            "a.safari",
            "a.safari",
            "a.vivaldi",
            "a.brave",
            "a.tor"
        ]

        for browser in browsers:
            self.assertTrue(is_element_present(
                self.driver,
                By.CSS_SELECTOR,
                browser)
            )

    def test_ad_mobile_links(self):
        platforms = ["a.apple", "a.google"]

        for platform in platforms:
            self.assertTrue(is_element_present(
                self.driver,
                By.CSS_SELECTOR,
                platform)
            )

    def test_ae_web_link(self):
        self.assertTrue(is_element_present(
            self.driver, By.XPATH, "//div[@id='download-web']//a[contains(@href, 'https://vault.bitwarden.com/#/')]"))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
