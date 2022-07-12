import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Функция для вычисления значения
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/math.html")
    # Извлекаем текст из тега
    element = browser.find_element(By.XPATH, "//span[@id='input_value']").text

    # Вычисляем функцию из этого числа
    value = calc(element)

    # Передаём значение в форму
    form = browser.find_element(By.XPATH, "//input")
    form.send_keys(value)

    # Отмечаем чекбокс
    check_box = browser.find_element(By.XPATH, "//input[@id='robotCheckbox']")
    check_box.click()

    # Отмечаем нужный радио баттон
    radio = browser.find_element(By.XPATH, "//input[@id='robotsRule']")
    radio.click()

    # Нажимаем на Submit
    submit = browser.find_element(By.XPATH, "//button[@type = 'submit']")
    submit.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()