from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
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
# для проверки, выводим значение в консоли
    print(z)
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()