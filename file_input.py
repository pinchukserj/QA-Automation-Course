from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")
    # заполняем поля Name, Surname, email
    browser.find_element(By.XPATH, "//input[@name='firstname']").send_keys('Serj')
    browser.find_element(By.XPATH, "//input[@name='lastname']").send_keys('Pinchuk')
    browser.find_element(By.XPATH, "//input[@name='email']").send_keys('mymail@gmail.com')
    # получаем путь к директории текущего исполняемого скрипта
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # имя файла, который будем загружать на сайт
    file_name = 'for_upload.txt'
    # получаем путь к for_upload.txt
    file_path = os.path.join(current_dir, file_name)
    # находим элемент для отправки файлов и отправляем наш файл
    browser.find_element(By.XPATH, "//input[@type='file']").send_keys(file_path)
    # нажимаем Submit
    browser.find_element(By.XPATH, "//button[@type = 'submit']").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()