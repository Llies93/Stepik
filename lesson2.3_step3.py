from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)


browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
browser.switch_to.alert.accept()
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)
browser.find_element(By.ID, 'answer').send_keys(y)
browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

time.sleep(10)
browser.quit()