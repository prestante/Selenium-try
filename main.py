from selenium import webdriver
import time

driver = webdriver.Chrome()
time.sleep(2)
driver.get("https://www.selenium.dev/selenium/web/web-form.html")
time.sleep(2)
title = driver.title
print(title)
time.sleep(2)
