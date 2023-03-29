# -*- coding: utf-8 -*-
import math

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(30)
    browser.get("https://stepik.org/lesson/236895/step/1")

    button = browser.find_element(By.ID, 'ember33')
    button.click()

    input1 = browser.find_element(By.NAME, "login")
    input1.send_keys("constantaasamara@gmail.com")
    input2 = browser.find_element(By.NAME, "password")
    input2.send_keys("624852Kostya12345")

    button = browser.find_element(By.XPATH, "//button[@class='sign-form__btn button_with-loader ' and @type='submit']")
    button.click()

    time.sleep(15)

    # Поиск элемента
    textarea = browser.find_element(By.CSS_SELECTOR, ".ember-text-area")

    # Ввод ответа и отправка
    answer = str(math.log(int(time.time())))
    print(answer)
    textarea.send_keys(answer)
    time.sleep(15)  # Оставляем время на проверку введенного текста перед отправкой

    button = browser.find_element(By.CSS_SELECTOR, ".submit-submission")
    button.click()


finally:
    time.sleep(100)
    browser.quit()
