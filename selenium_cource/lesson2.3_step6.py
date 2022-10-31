'''
Сценарий для реализации выглядит так:
1 Открыть страницу http://suninjuly.github.io/redirect_accept.html
2 Нажать на кнопку
3 Переключиться на новую вкладку
4 Пройти капчу для робота и получить число-ответ
'''

# сам код по заданию
import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

try:
    #1
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
  
    #2
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    
    #3
    # запомнить имя текущей вкладки
    first_window = browser.window_handles[0]
    # Чтобы узнать имя новой вкладки, нужно использовать метод window_handles, который возвращает массив имён всех вкладок
    new_window = browser.window_handles[1]
    # Для переключения на новую вкладку надо явно указать, на какую вкладку мы хотим перейти
    browser.switch_to.window(new_window)
    
    #4-1
    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))
    element_x = browser.find_element(By.ID, "input_value")
    x = element_x.text
    y = calc(x)
    
    #4-2
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    
    #5 Нажать кнопку "Submit"
    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()