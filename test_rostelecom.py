import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(r'/home/panda/Documents/inga/selenium/chromedriver/chromedriver')
auth_url = 'https://b2c.passport.rt.ru'

@pytest.fixture(scope='session', autouse=True)
def driver():
    driver = webdriver.Chrome(r'/home/panda/Documents/inga/selenium/chromedriver/chromedriver')

    yield driver
    driver.quit()

# 1 Проверка поля "Имя" соответствующего требованиям
def test_valid_name(driver):
    name = "Иван"
    driver.get(auth_url)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "kc-register"))).click()
    name_input = driver.find_element(By.XPATH, "//input[@name='firstName']")
    name_input.send_keys(name)
    assert name_input.get_attribute("value") == name

# 2 Проверка поля "Имя" содержащего одну букву
def test_invalid_name_one_letter(driver):
    name = "И"
    expected_error = "Необходимо заполнить поле кириллицей. От 2 до 30 символов."
    driver.get(auth_url)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "kc-register"))).click()
    name_input = driver.find_element(By.XPATH, "//input[@name='firstName']")
    name_input.send_keys(name)
    error_message = driver.find_element(By.XPATH, "//span[@class='rt-input-container__meta rt-input-container__meta--error']").text
    assert error_message == expected_error

# 3 Проверка поля "Имя" содержащего цифры, латинские буквы
def test_invalid_latin_name(driver):
    name = "ivan2"
    expected_error = "Необходимо заполнить поле кириллицей. От 2 до 30 символов."
    driver.get(auth_url)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "kc-register"))).click()
    name_input = driver.find_element(By.XPATH, "//input[@name='firstName']")
    name_input.send_keys(name)
    error_message = driver.find_element(By.XPATH, "//span[@class='rt-input-container__meta rt-input-container__meta--error']").text
    assert error_message == expected_error

#4 Проверка пустого поля "Имя"
def test_empty_name(driver):
    expected_error = "Необходимо заполнить поле кириллицей. От 2 до 30 символов."
    driver.get(auth_url)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "kc-register"))).click()
    name_input = driver.find_element(By.XPATH, "//input[@name='firstName']")
    name_input.send_keys(Keys.ENTER)
    error_message = driver.find_element(By.XPATH,
                                        "//span[@class='rt-input-container__meta rt-input-container__meta--error']").text
    assert error_message == expected_error

# 5 Проверка поля "Имя" при вводе 31 буквы
def test_invalid_name_lengh(driver):
    name = "Иваниваниваниваниваниваниванива"
    expected_error = "Необходимо заполнить поле кириллицей. От 2 до 30 символов."
    driver.get(auth_url)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "kc-register"))).click()
    name_input = driver.find_element(By.XPATH, "//input[@name='firstName']")
    name_input.send_keys(name)
    error_message = driver.find_element(By.XPATH,
                                        "//span[@class='rt-input-container__meta rt-input-container__meta--error']").text
    assert error_message == expected_error

# 6 Проверка поля "Имя" при вводе 30 букв
def test_valid_name_lengh(driver):
    name = "Иваниваниваниваниваниваниванив"
    driver.get(auth_url)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "kc-register"))).click()
    name_input = driver.find_element(By.XPATH, "//input[@name='firstName']")
    name_input.send_keys(name)
    assert name_input.get_attribute("value") == name


# 7 Проверка поля "Фамилия" соответствующего требованиям
def test_valid_lastname(driver):
    lastname = "Ив"
    driver.get(auth_url)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "kc-register"))).click()
    lastname_input = driver.find_element(By.XPATH, "//input[@name='lastName']")
    lastname_input.send_keys(lastname)
    assert lastname_input.get_attribute("value") == lastname

# 9 Проверка поля "Фамилия" состоящего из одной буквы
def test_invalid_lastname_one_letter(driver):
    lastname = "И"
    expected_error = "Необходимо заполнить поле кириллицей. От 2 до 30 символов."
    driver.get(auth_url)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "kc-register"))).click()
    lastname_input = driver.find_element(By.XPATH, "//input[@name='lastName']")
    lastname_input.send_keys(lastname)
    error_message = driver.find_element(By.XPATH, "//span [@class='rt-input-container__meta rt-input-container__meta--error']").text
    assert error_message == expected_error

# 10 Проверка поля "Фамилия" состоящего из латинских букв
def test_invalid_lastname(driver):
    lastname = "ivanov"
    expected_error = "Необходимо заполнить поле кириллицей. От 2 до 30 символов."
    driver.get(auth_url)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "kc-register"))).click()
    lastname_input = driver.find_element(By.XPATH, "//input[@name='lastName']")
    lastname_input.send_keys(lastname)
    error_message = driver.find_element(By.XPATH, "//span [@class='rt-input-container__meta rt-input-container__meta--error']").text
    assert error_message == expected_error

# 11 Проверка поля "Фамилия" состоящего из 30 букв
def test_valid_lastname_lengh(driver):
    lastname = "Иваниваниваниваниваниваниванив"
    driver.get(auth_url)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "kc-register"))).click()
    lastname_input = driver.find_element(By.XPATH, "//input[@name='lastName']")
    lastname_input.send_keys(lastname)
    assert lastname_input.get_attribute("value") == lastname

# 12 Проверка поля "Email или мобильный телефон" с некорректными данными
def test_invalid_contact(driver):
    contact_info = "fghghhgmai.com"
    expected_error = "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru"
    driver.get(auth_url)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "kc-register"))).click()
    contact_input = driver.find_element(By.ID, "address")
    contact_input.send_keys(contact_info)
    error_message = driver.find_element(By.XPATH, "//span[@class='rt-input-container__meta rt-input-container__meta--error']").text
    assert error_message == expected_error

# 13  Проверка поля "Email или мобильный телефон" с корректными данным
def test_valid_contact(driver):
    contact_info = "+79123456789"
    driver.get(auth_url)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "kc-register"))).click()
    contact_input = driver.find_element(By.ID, "address")
    contact_input.send_keys(contact_info)
    assert contact_input.get_attribute("value") == contact_info

# 14  Проверка поля "Email или мобильный телефон" с корректными данным
def test_valid_contact_email(driver):
    contact_info = "test@gmail.com"
    driver.get(auth_url)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "kc-register"))).click()
    contact_input = driver.find_element(By.ID, "address")
    contact_input.send_keys(contact_info)
    assert contact_input.get_attribute("value") == contact_info

# 15 Проверка поля "пароль" состоящего из 7 чисел
def test_short_password(driver):
    password = "1234567"
    expected_error = "Длина пароля должна быть не менее 8 символов"
    driver.get(auth_url)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "kc-register"))).click()
    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys(password)
    error_message = driver.find_element(By.XPATH, "//span[@class='rt-input-container__meta rt-input-container__meta--error']").text
    assert error_message ==expected_error

# 16 Проверка поля "Пароль" состоящего только из чисел
def test_password_no_uppercase(driver):
    password = "12345678"
    expected_error = "Пароль должен содержать хотя бы одну заглавную букву"
    driver.get(auth_url)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "kc-register"))).click()
    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys(password)
    error_message = driver.find_element(By.XPATH,
                                        "//span[@class='rt-input-container__meta rt-input-container__meta--error']").text
    assert error_message == expected_error

# 17 Проверка поля "Пароль" с кириллицей
def test_non_latin_characters(driver):
    password = "12345678П"
    expected_error = "Пароль должен содержать только латинские буквы"
    driver.get(auth_url)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "kc-register"))).click()
    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys(password)
    error_message = driver.find_element(By.XPATH,
                                        "//span[@class='rt-input-container__meta rt-input-container__meta--error']").text
    assert error_message == expected_error

# 18 Проверка поля "пароль" соответствующего требованиям
def test_valid_password(driver):
    password = "12345678Qq"
    driver.get(auth_url)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "kc-register"))).click()
    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys(password)
    assert password_input.get_attribute("value") == password

# 19 Проверка поля "подтверждение пароля"
def test_password_mismatch(driver):
    new_password = "12345678Qq"
    confirm_password = "12345678qQ"
    expected_error = "Пароли не совпадают"
    driver.get(auth_url)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "kc-register"))).click()
    new_password_input = driver.find_element(By.ID, "password")
    confirm_password_input = driver.find_element(By.ID, "password-confirm")
    new_password_input.send_keys(new_password)
    confirm_password_input.send_keys(confirm_password)
    error_message = driver.find_element(By.XPATH, "//span[@class='rt-input-container__meta rt-input-container__meta--error']").text
    assert error_message == expected_error

# 20 Проверка кликабельности ссылки на пользовательскоей соглашение
def test_clickable_user_agreement(driver):
    driver.get(auth_url)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@class='user-agreement-link']"))).click()

# 21 Проверка кликабельности "забыли пароль"
def test_clickable_forgot_password(driver):
    driver.get(auth_url)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "forgot_password"))).click()

# 22 Проверка кликабельности табов
def test_clickable_tabs(driver):
    driver.get(auth_url)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "t-btn-tab-phone"))).click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "t-btn-tab-mail"))).click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "t-btn-tab-login"))).click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "t-btn-tab-ls"))).click()

# 23 Регистрация пользователя
def test_registration(driver):
    name = "Иван"
    lastname = "Иванов"
    contact = "+79123456789"
    password = "12345678Qq"
    confirm = "12345678Qq"
    error = driver.find_element(By.XPATH, "//h2[@class='card-modal__title']").text
    driver.get(auth_url)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "kc-register"))).click()
    name_input = driver.find_element(By.XPATH, "//input[@name='firstName']")
    name_input.send_keys(name)
    lastname_input = driver.find_element(By.XPATH, "//input[@name='lastName']")
    lastname_input.send_keys(lastname)
    contact_input = driver.find_element(By.ID, "address")
    contact_input.send_keys(contact)
    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys(password)
    confirm_input = driver.find_element(By.ID,"password-confirm")
    confirm_input.send_keys(confirm)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@class ='rt-btn rt-btn--orange rt-btn--medium rt-btn--rounded register-form__reg-btn']"))).click()


# 24 Проверка авторизации зарегистрированного пользователя
def test_auth(driver):
    contact = "+79123456789"
    password = "12345678Qq"
    driver.get(auth_url)
    contact_input = driver.find_element(By.ID, 'username')
    contact_input.send_keys(contact)
    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys(password)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'kc-login'))).click()

