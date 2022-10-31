'''
1 Открыть страницу http://suninjuly.github.io/alert_accept.html
2 Нажать на кнопку
3 Принять confirm
4 На новой странице решить капчу для роботов, чтобы получить число с ответом
'''

# сам код по заданию
import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

try:
    #1
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
  
    #2
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    
    #3
    confirm = browser.switch_to.alert
    confirm.accept()
    
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