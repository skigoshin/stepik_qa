'''
!!!    Автотест упадет с сообщением NoSuchElementException для элемента c id="verify" так задумано   !!!
Тестовый сценарий выглядит так:
Открыть страницу http://suninjuly.github.io/wait1.html
Нажать на кнопку "Verify"
Проверить, что появилась надпись "Verification was successful!"
'''

# сам код по заданию
import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/wait1.html")

    button = browser.find_element(By.ID, "verify")
    button.click()
    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()