from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)

    #вводим ответ в текстовое поле
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)

    #находим кнопку и скроллим к ней
    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"].btn')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    #кликаем на чекбокс
    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    option1.click()

    #кликаем на радиобаттон
    option1 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    option1.click()

    # Нажимаем сабмит
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()