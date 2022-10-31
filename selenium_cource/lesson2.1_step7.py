from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Посчитать математическую функцию от x
    import math

    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))
      
    # Найти на ней элемент-картинку, который является изображением сундука с сокровищами
    #src="images/chest.png"
    images = browser.find_element(By.ID, "treasure")
    # Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
    x = images.get_attribute("valuex")
    y = calc(x)
    # Посчитать математическую функцию от x (сама функция остаётся неизменной).
    # Прописана в начале кода.
    
    # Ввести ответ в текстовое поле.
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    
    # Отметить checkbox "I'm the robot".
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    # Выбрать radiobutton "Robots rule!".
    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()

    # Нажать на кнопку "Submit".
    submit = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit.click()
    
    # ждем загрузки страницы
    time.sleep(3)

  
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()