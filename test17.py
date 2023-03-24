# -*- coding: utf-8 -*-
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class Test(unittest.TestCase):
    def test(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.CSS_SELECTOR, "input.first[required]")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, "input.second[required]")
        input2.send_keys("Ivanov")
        input3 = browser.find_element(By.CSS_SELECTOR, "input.third[required]")
        input3.send_keys("JJJ@gmail.com")
        input5 = browser.find_element(By.CSS_SELECTOR, "input.second[required]")
        input5.send_keys("mayami")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(5)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!" == welcome_text)

    def test_abs2(self):
        def test(self):
            link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            input1 = browser.find_element(By.CSS_SELECTOR, "input.first[required]")
            input1.send_keys("Ivan")
            input2 = browser.find_element(By.CSS_SELECTOR, "input.second[required]")
            input2.send_keys("Ivanov")
            input3 = browser.find_element(By.CSS_SELECTOR, "input.third[required]")
            input3.send_keys("JJJ@gmail.com")
            input5 = browser.find_element(By.CSS_SELECTOR, "input.second[required]")
            input5.send_keys("mayami")

            # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(5)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            self.assertEqual("Congratulations! You have successfully registered!" == welcome_text)


if __name__ == "__main__":
    pytest.main()