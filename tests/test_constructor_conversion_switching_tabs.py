from conftest import driver
from locators import Locators
from constants import ConstantsUrl
from selenium.webdriver.common.by import By


class TestConstructorSwitchingTabs:
    def test_costractor_tab_fillings(self, driver):
        driver.get(ConstantsUrl.start_page_url)
        driver.find_element(By.XPATH, Locators.constructor_button).click()
        driver.find_element(By.XPATH, Locators.tab_filling).click()
        assert driver.find_element(By.XPATH, Locators.tab_active_current).text in 'Начинки'


    def test_costractor_tab_sauce(self, driver):
        driver.get(ConstantsUrl.start_page_url)
        driver.find_element(By.XPATH, Locators.constructor_button).click()
        driver.find_element(By.XPATH, Locators.tab_sauce).click()
        assert driver.find_element(By.XPATH, Locators.tab_active_current).text in 'Соусы'


    def test_costractor_tab_buns(self, driver):
        driver.get(ConstantsUrl.start_page_url)
        driver.find_element(By.XPATH, Locators.constructor_button).click()
        driver.find_element(By.XPATH, Locators.tab_filling).click()
        driver.find_element(By.XPATH, Locators.tab_buns).click()
        assert driver.find_element(By.XPATH, Locators.tab_active_current).text in 'Булки'
