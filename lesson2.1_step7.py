from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
treasure = browser.find_element(By.ID, "treasure")
x_element = treasure.get_attribute("valuex")
x = x_element
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
