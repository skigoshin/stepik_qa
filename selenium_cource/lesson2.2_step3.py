from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    #link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)


    # находим первое значение
    x_element = browser.find_element(By.CSS_SELECTOR, "#num1")
    # берем текст первого значения
    x = x_element.text
    # находим второе значение
    y_element = browser.find_element(By.CSS_SELECTOR, "#num2")
    # берем текст второго значения
    y = y_element.text
    # складываем значения
    z = str(int(x)+int(y))

    print(z)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(z)) # ищем и выбираем значение z

    
    # находим и кликаем по кнопке Submit
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()