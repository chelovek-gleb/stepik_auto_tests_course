from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

try: 
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x_element = browser.find_element(By.ID, 'num1').text
    x1_element = browser.find_element(By.ID, 'num2').text
    su=int(x_element)+int(x1_element)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(su))
    

    # Нажимаем сабмит
    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"].btn')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()