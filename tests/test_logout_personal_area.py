from conftest import driver
from locators import Locators
from constants import ConstantsUrl
from constants import ConstantsTestData
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLogout:
    def test_logout_from_personal_area(self,driver):
        driver.get(ConstantsUrl.login_page_url)
        WebDriverWait(driver, 3).until(EC.url_contains(ConstantsUrl.login_page_url))
        driver.find_element(By.XPATH, Locators.authorization_field_login).send_keys(ConstantsTestData.user_email)
        driver.find_element(By.XPATH, Locators.authorization_field_password).send_keys(ConstantsTestData.user_password)
        driver.find_element(By.XPATH, Locators.enter_button).click()
        WebDriverWait(driver, 7).until(EC.url_to_be(ConstantsUrl.start_page_url))
        driver.get(ConstantsUrl.profile_page_url)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, Locators.exit_button)))
        driver.find_element(By.XPATH, Locators.exit_button).click()
        WebDriverWait(driver, 3).until(EC.url_contains(ConstantsUrl.login_page_url))
        assert driver.current_url == ConstantsUrl.login_page_url

