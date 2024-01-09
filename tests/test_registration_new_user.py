from conftest import driver
from selenium.webdriver.common.by import By
from constants import ConstantsUrl
from locators import Locators
from random_test_credentials import RandomTestCredentials
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class TestRegistration:
    def test_registration_new_user_correct_credentials(self, driver):
        driver.get(ConstantsUrl.start_page_url)
        driver.find_element(By.XPATH, Locators.personal_area_button).click()
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, Locators.register_link)))
        driver.find_element(By.XPATH, Locators.register_link).click()

        """
        Получаем рандомные креды, сохраняем их в переменные, для того что бы использовать их дважды
        1 раз для того что бы зарегистироваться
        2 раз для того что бы проверить успешную регистрацию и авторизоваться
        """

        name = RandomTestCredentials.name
        email = RandomTestCredentials.email
        password = RandomTestCredentials.password

        driver.find_element(By.XPATH, Locators.entry_field_user_name).send_keys(name)
        driver.find_element(By.XPATH, Locators.entry_field_user_email).send_keys(email)
        driver.find_element(By.XPATH, Locators.entry_field_user_password).send_keys(password)
        driver.find_element(By.XPATH, Locators.register_button).click()
        WebDriverWait(driver, 3).until(EC.url_contains(ConstantsUrl.login_page_url))
        driver.find_element(By.XPATH, Locators.authorization_field_login).send_keys(email)
        driver.find_element(By.XPATH, Locators.authorization_field_password).send_keys(password)
        driver.find_element(By.XPATH, Locators.enter_button).click()

        """
        После того как зарегистрировались и вошли в кабинет, проверем что на главной странице отстутсвует кнопка
        войти в аккаунт
        """

        element = WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.XPATH, Locators.design_order)))
        assert element.text == "Оформить заказ"


    def test_registration_incorrect_password_error(self, driver):
        driver.get(ConstantsUrl.start_page_url)
        driver.find_element(By.XPATH, Locators.personal_area_button).click()
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, Locators.register_link)))
        driver.find_element(By.XPATH, Locators.register_link).click()
        driver.find_element(By.XPATH, Locators.entry_field_user_name).send_keys(RandomTestCredentials.name)
        driver.find_element(By.XPATH, Locators.entry_field_user_email).send_keys(RandomTestCredentials.email)
        driver.find_element(By.XPATH, Locators.entry_field_user_password).send_keys(RandomTestCredentials.incorrect_password)
        driver.find_element(By.XPATH, Locators.register_button).click()
        driver.find_element(By.XPATH, Locators.register_button).click()
        assert driver.find_element(By.XPATH, Locators.registration_message_error).text == 'Некорректный пароль'