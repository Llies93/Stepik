from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)



z_element = browser.find_element(By.ID, "num1")
y_element = browser.find_element(By.ID, "num2")
z = z_element.text
y = y_element.text
sum = str(int(z) + int(y))


select = Select(browser.find_element(By.ID, "dropdown"))
select.select_by_value(str(sum))
button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
button.click()

time.sleep(10)

browser.quit()

