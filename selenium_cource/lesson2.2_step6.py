from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


try:
    #1 Открыть в браузере страницу http://SunInJuly.github.io/execute_script.html.
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #2 Считать значение для переменной x.
    x_element = browser.find_element(By.ID, "input_value")
    # берем текст первого значения
    x = x_element.text

    #3 Посчитать математическую функцию от x.
    import math
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    y = calc(x)
    # Атрибут text возвращает текст, который находится между открывающим и закрывающим тегами элемента. 
    # Пример: <div class="message">У вас новое сообщение.</div> вернёт строку: "У вас новое сообщение"



    #5 Ввести ответ в текстовое поле.
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    #4 Проскроллить страницу
    browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
    input1.send_keys(str(y))

    #6 Выбрать checkbox "I'm the robot".
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()
    

    #7 Переключить radiobutton "Robots rule!".
    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()
 

    #8 Нажать на кнопку "Submit".
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()