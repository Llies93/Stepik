from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

browser.find_element(By.CSS_SELECTOR, 'input[name="firstname"]').send_keys("Михаилпетрович")
browser.find_element(By.CSS_SELECTOR, "input[name='lastname']").send_keys("Зубенко")
browser.find_element(By.CSS_SELECTOR, 'input[name="email"]').send_keys("мыло")

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')

browser.find_element(By.ID, "file").send_keys(file_path)
browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

time.sleep(10)
browser.quit()