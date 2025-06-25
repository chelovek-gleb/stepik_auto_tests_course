from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Нажимаем сабмит
    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"].btn')
    button.click()

    # Переключаемся на модальное окно и нажимаем ок(подтверждаем)
    confirm = browser.switch_to.alert
    confirm.accept()

    # Находим текстовое значение и Высчитываем по формуле
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)

    #вводим ответ в текстовое поле
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)

    # Нажимаем сабмит
    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"].btn')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()