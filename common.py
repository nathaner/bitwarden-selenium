from selenium.common.exceptions import NoSuchElementException


def is_element_present(driver, how, what):
    try:
        driver.find_element(by=how, value=what)
    except NoSuchElementException:
        return False
    return True
