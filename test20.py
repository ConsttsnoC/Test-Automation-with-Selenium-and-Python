# -*- coding: utf-8 -*-
import math
import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.fixture(params=['https://stepik.org/lesson/236895/step/1',
         'https://stepik.org/lesson/236896/step/1',
         'https://stepik.org/lesson/236897/step/1',
         'https://stepik.org/lesson/236898/step/1',
         'https://stepik.org/lesson/236899/step/1',
         'https://stepik.org/lesson/236903/step/1',
         'https://stepik.org/lesson/236904/step/1',
         'https://stepik.org/lesson/236905/step/1'])
def link(request):
    return request.param

def test_stepik_feedback(browser, link):
    browser.get(link)

    button = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'ember33')))
    button.click()

    input1 = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, "login")))
    input1.send_keys("constantaasamara@gmail.com")
    input2 = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, "password")))
    input2.send_keys("624852Kostya12345")

    button = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,"//button[@class='sign-form__btn button_with-loader ' and @type='submit']")))
    button.click()

    time.sleep(20)

    textarea = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".ember-text-area")))

    # Ввод ответа и отправка
    answer = str(math.log(int(time.time())))
    textarea.send_keys(answer)
    time.sleep(10)

    button = browser.find_element(By.CSS_SELECTOR, ".submit-submission")
    button.click()

    feedback = browser.find_element(By.CLASS_NAME, "smart-hints__hint").text
    assert feedback == "Correct!", "Feedback doesn't have correct word"