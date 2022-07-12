from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

try:
  browser = webdriver.Chrome()
  browser.get("http://suninjuly.github.io/selects1.html")
  # Складываем два значения, предварительно переводим в int
  value = int(browser.find_element(By.XPATH, "//span[@id='num1']").text) + int(browser.find_element(By.XPATH, "//span[@id='num2']").text)

  # Инициализируем объект с тегом select
  select = Select(browser.find_element(By.TAG_NAME, "select"))

  # Выбираем по значению
  select.select_by_value(str(value))

  # Нажимаем на Submit
  submit = browser.find_element(By.XPATH, "//button[@type = 'submit']").click()


finally:
  # успеваем скопировать код за 8 секунд
  time.sleep(8)
  # закрываем браузер после всех манипуляций
  browser.quit()