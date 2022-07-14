from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

# Функция для вычисления значения
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    # нажимаем на кнопку
    browser.find_element(By.TAG_NAME, 'button').click()
    # переключаемся на открывшуюся вкладку (создаётся массив window_handles)
    browser.switch_to.window(browser.window_handles[1])
    # извлекаем текст из тега
    element = browser.find_element(By.XPATH, "//span[@id='input_value']").text
    # Вычисляем функцию из этого числа
    value = calc(element)
    # Передаём значение в форму
    form = browser.find_element(By.XPATH, "//input")
    form.send_keys(value)
    # Нажимаем на Submit
    submit = browser.find_element(By.XPATH, "//button[@type = 'submit']").click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()