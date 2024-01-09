from conftest import driver
from locators import Locators
from constants import ConstantsUrl
from constants import ConstantsTestData
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestNavigation:
    def test_conversion_navigation_in_personal_area(self, driver):
        driver.get(ConstantsUrl.start_page_url)
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, Locators.personal_area_button)))
        driver.find_element(By.XPATH, Locators.personal_area_button).click()
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, Locators.enter_button)))
        driver.find_element(By.XPATH, Locators.authorization_field_login).send_keys(ConstantsTestData.user_email)
        driver.find_element(By.XPATH, Locators.authorization_field_password).send_keys(ConstantsTestData.user_password)
        driver.find_element(By.XPATH, Locators.enter_button).click()
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, Locators.personal_area_button)))
        driver.find_element(By.XPATH, Locators.personal_area_button).click()
        element = WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.XPATH, Locators.profile_header)))
        assert element.text == "Профиль"


    def test_conversion_navigation_from_personal_area_to_constructor(self, driver):
        driver.get(ConstantsUrl.start_page_url)
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, Locators.personal_area_button)))
        driver.find_element(By.XPATH, Locators.personal_area_button).click()
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, Locators.enter_button)))
        driver.find_element(By.XPATH, Locators.authorization_field_login).send_keys(ConstantsTestData.user_email)
        driver.find_element(By.XPATH, Locators.authorization_field_password).send_keys(ConstantsTestData.user_password)
        driver.find_element(By.XPATH, Locators.enter_button).click()
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, Locators.personal_area_button)))
        driver.find_element(By.XPATH, Locators.personal_area_button).click()
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, Locators.constructor_button)))
        driver.find_element(By.XPATH, Locators.constructor_button).click()
        element = WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.XPATH, Locators.constructor_header)))
        assert element.text == "Соберите бургер"


    def test_conversion_navigation_from_personal_area_to_logo_start_page(self, driver):
        driver.get(ConstantsUrl.start_page_url)
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, Locators.personal_area_button)))
        driver.find_element(By.XPATH, Locators.personal_area_button).click()
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, Locators.enter_button)))
        driver.find_element(By.XPATH, Locators.authorization_field_login).send_keys(ConstantsTestData.user_email)
        driver.find_element(By.XPATH, Locators.authorization_field_password).send_keys(ConstantsTestData.user_password)
        driver.find_element(By.XPATH, Locators.enter_button).click()
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, Locators.personal_area_button)))
        driver.find_element(By.XPATH, Locators.personal_area_button).click()
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, Locators.logo_image_button)))
        driver.find_element(By.XPATH, Locators.logo_image_button).click()
        element = WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.XPATH, Locators.design_order)))
        assert element.text == "Оформить заказ"
