from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
x_element = browser.find_element(By.CSS_SELECTOR, "span[id='input_value']")
x = x_element.text
y = calc(x)
try:

    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)
    checkbox = browser.find_element(By.CSS_SELECTOR, 'input[type="checkbox"]')
    checkbox.click()
    radiobutt = browser.find_element(By.ID, 'robotsRule')
    radiobutt.click()
    button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    button.click()

finally:
    time.sleep(5)

    browser.quit()
