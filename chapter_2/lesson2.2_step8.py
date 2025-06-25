from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #ищем поля для ввода и вводим инфу
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("test@gmail.com")
    input4 = browser.find_element(By.ID, "file")
    input4.send_keys("D:\MyPythonProjects\Selenium_lessons/otpravka.txt")

    #Ищем и нажимаем кнопку
    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"].btn')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()