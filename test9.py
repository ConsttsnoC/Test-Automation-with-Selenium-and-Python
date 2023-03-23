# -*- coding: utf-8 -*-
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x = int(browser.find_element(By.CSS_SELECTOR, '#num1').text)
    y = int(browser.find_element(By.CSS_SELECTOR, '#num2').text)


    def calc(x, y):
        return int(x + y)


    result = calc(x, y)
    print(result)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(result))

    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()