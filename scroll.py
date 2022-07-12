import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Функция для вычисления значения
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/execute_script.html")
    # Забираем значение
    x = int(browser.find_element(By.XPATH, "//*[@id='input_value']").text)
    value = calc(x)
    # Заполняем поле
    form = browser.find_element(By.XPATH, "//*[@id='answer']")
    form.send_keys(value)
    # Скроллим к кнопке с помощью JS скрипта
    submit_button = browser.find_element(By.XPATH, "//*[@type='submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit_button)

    # Отмечаем чекбокс
    check_box = browser.find_element(By.XPATH, "//input[@id='robotCheckbox']")
    check_box.click()

    # Отмечаем нужный радио баттон, проскроллив к нему
    radio = browser.find_element(By.XPATH, "//*[@id='robotsRule']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
    radio.click()
    submit_button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()