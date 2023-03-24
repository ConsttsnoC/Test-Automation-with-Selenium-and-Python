# -*- coding: utf-8 -*-
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.XPATH, "//button[text()='I want to go on a magical journey!']")
    button.click()



    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    time.sleep(2)

    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    print(calc(x))
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(calc(x))

    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()