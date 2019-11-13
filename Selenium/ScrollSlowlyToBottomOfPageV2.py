# Scroll Slowly to the bottom of a page
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.by import By # include by implementation
import urllib.request
import time

# Requires chrome web driver path to work on using Chrome
chromeDriverLocation = './chromedriver'
# Create a new instance of the Chrome driver
driver = webdriver.Chrome(chromeDriverLocation)

# go to imgur's website
driver.get("https://imgur.com/gallery/P5JAMjr")
pages_remaining = True

y = 1000

while pages_remaining:
    try:
        old_position = driver.execute_script(
                ("return (window.pageYOffset !== undefined) ?"
                 " window.pageYOffset : (document.documentElement ||"
                 " document.body.parentNode || document.body);"))
        print("old_position:", old_position)

        driver.execute_script("window.scrollTo(0, "+str(y)+")")
        y += 1000
        time.sleep(1)

        new_position = driver.execute_script(
                ("return (window.pageYOffset !== undefined) ?"
                 " window.pageYOffset : (document.documentElement ||"
                 " document.body.parentNode || document.body);"))
        print("new_position:", new_position)

        if new_position == old_position:
            break

    except (TimeoutException, WebDriverException) as e:
        print("Last page reached")
        break

driver.quit()
