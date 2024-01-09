from conftest import driver
from locators import Locators
from constants import ConstantsUrl
from constants import ConstantsTestData
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestEntrance:
    def test_entrance_personal_area_using_button_personal_area_on_the_main_page(self, driver):
        driver.get(ConstantsUrl.start_page_url)
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, Locators.personal_area_button)))
        driver.find_element(By.XPATH, Locators.personal_area_button).click()
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, Locators.enter_button)))
        driver.find_element(By.XPATH, Locators.authorization_field_login).send_keys(ConstantsTestData.user_email)
        driver.find_element(By.XPATH, Locators.authorization_field_password).send_keys(ConstantsTestData.user_password)
        driver.find_element(By.XPATH, Locators.enter_button).click()
        element = WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.XPATH, Locators.design_order)))
        assert element.text == "Оформить заказ"


    def test_entrance_personal_area_using_button_enter_to_account_on_the_main_page(self, driver):
        driver.get(ConstantsUrl.start_page_url)
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, Locators.personal_area_button)))
        driver.find_element(By.XPATH, Locators.personal_area_button).click()
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, Locators.enter_button)))
        driver.find_element(By.XPATH, Locators.authorization_field_login).send_keys(ConstantsTestData.user_email)
        driver.find_element(By.XPATH, Locators.authorization_field_password).send_keys(ConstantsTestData.user_password)
        driver.find_element(By.XPATH, Locators.enter_button).click()
        element = WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.XPATH, Locators.design_order)))
        assert element.text == "Оформить заказ"


    def test_entrance_personal_area_using_button_in_the_registration_form(self,driver):
        driver.get(ConstantsUrl.start_page_url)
        driver.find_element(By.XPATH, Locators.personal_area_button).click()
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, Locators.register_link)))
        driver.find_element(By.XPATH, Locators.register_link).click()
        driver.find_element(By.XPATH, Locators.enter_link).click()
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, Locators.enter_button)))
        driver.find_element(By.XPATH, Locators.authorization_field_login).send_keys(ConstantsTestData.user_email)
        driver.find_element(By.XPATH, Locators.authorization_field_password).send_keys(ConstantsTestData.user_password)
        driver.find_element(By.XPATH, Locators.enter_button).click()
        element = WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.XPATH, Locators.design_order)))
        assert element.text == "Оформить заказ"


    def test_entrance_personal_area_using_button_in_the_password_recovery_form(self,driver):
        driver.get(ConstantsUrl.start_page_url)
        driver.find_element(By.XPATH, Locators.personal_area_button).click()
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, Locators.password_recovery_link)))
        driver.find_element(By.XPATH, Locators.password_recovery_link).click()
        driver.find_element(By.XPATH, Locators.enter_link).click()
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, Locators.enter_button)))
        driver.find_element(By.XPATH, Locators.authorization_field_login).send_keys(ConstantsTestData.user_email)
        driver.find_element(By.XPATH, Locators.authorization_field_password).send_keys(ConstantsTestData.user_password)
        driver.find_element(By.XPATH, Locators.enter_button).click()
        element = WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.XPATH, Locators.design_order)))
        assert element.text == "Оформить заказ"
