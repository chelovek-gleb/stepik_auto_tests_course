from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # Нажимаем сабмит
    button = browser.find_element(By.ID, "book")
    button.click()

    # Находим текстовое значение и Высчитываем по формуле
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    # вводим ответ в текстовое поле
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)

    # Нажимаем сабмит
    button1 = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button1.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
