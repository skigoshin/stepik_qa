# Описание из комментария, как это работает
'''
3.путь автоматизатора.
если файлы lesson2_7.py и file_example.txt" лежат в одном каталоге
# импортируем модуль
import os
# получаем путь к директории текущего исполняемого скрипта lesson2_7.py
current_dir = os.path.abspath(os.path.dirname(__file__))
# имя файла, который будем загружать на сайт
file_name = "file_example.txt"
# получаем путь к file_example.txt
file_path = os.path.join(current_dir, file_name)
# находим кнопку
element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
# отправляем файл
element.send_keys(file_path)
"""
итоговый код:
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Firefox()
browser.get(link)
current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = "file_example.txt"
file_path = os.path.join(current_dir, file_name)
element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
element.send_keys(file_path)
'''

# сам код по заданию
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time

try:
    #1 Открыть страницу http://suninjuly.github.io/file_input.html
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #2 Заполнить текстовые поля: имя, фамилия, email
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("имя")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("фамилия")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("email")
    
    #3 Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
    current_dir = os.path.abspath(os.path.dirname('lesson2.2_step8-test.py'))
    file_name = "test.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)
    
    #4 Нажать кнопку "Submit"
    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()