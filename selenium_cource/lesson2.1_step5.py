from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    

    # Посчитать математическую функцию от x
    import math

    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))
    
    # Считать значение для переменной x
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    # Атрибут text возвращает текст, который находится между открывающим и закрывающим тегами элемента. 
    # Пример: <div class="message">У вас новое сообщение.</div> вернёт строку: "У вас новое сообщение"
 

   
    # Ввести ответ в текстовое поле.
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)
    
    # Отметить checkbox "I'm the robot"
    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()
    
    # Выбрать radiobutton "Robots rule!".
    option2 = browser.find_element(By.ID, "robotsRule")
    option2.click()
    
    
    # Нажать на кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # ждем загрузки страницы
    time.sleep(3)

  
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()