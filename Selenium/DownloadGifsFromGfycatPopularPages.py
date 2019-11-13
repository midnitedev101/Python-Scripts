from selenium import webdriver
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.by import By # include by implementation
import urllib.request
import random
import string
import os
import time
import requests # install requests module first
from datetime import datetime, timedelta
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# import keyboard
# from selenium.webdriver.common.keys import Keys



def randomStringDigits(stringLength=6):
    """Generate a random string of letters and digits """
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

# Create a new instance of the Firefox driver
# driver = webdriver.Firefox()

chromeDriverLocation = './chromedriver'
# Create a new instance of the Chrome driver
driver = webdriver.Chrome(chromeDriverLocation)

# driver.implicitly_wait(30) # seconds

# go to gfycat's trending page
driver.get("https://gfycat.com/popular-gifs")

SCROLL_PAUSE_TIME = 3
# last_height = driver.execute_script("return document.body.scrollHeight")
#
# Get current directory
currentDirectory = os.getcwd()
gifPath = currentDirectory + "/gifs/"

# Checks if video path exists, if not create it
if not os.path.exists(gifPath):
    print("creating directory...")
    os.mkdir(gifPath)

gifurls = []

y = 1000

# Define time_end which will run for 3 seconds (can change to any value, depends on device storage capacity)
time_end = datetime.now() + timedelta(seconds=3)
while datetime.now() < time_end:
    try:
        old_position = driver.execute_script(
                ("return (window.pageYOffset !== undefined) ?"
                 " window.pageYOffset : (document.documentElement ||"
                 " document.body.parentNode || document.body);"))

        gifLinks = driver.find_elements_by_css_selector("img.image.media")

        for gifLink in gifLinks:
            if gifLink.get_attribute("src") is not None:
                gifurls.append(gifLink.get_attribute("src"))

        driver.execute_script("window.scrollTo(0, "+str(y)+")")
        y += 1000
        time.sleep(1)

        new_position = driver.execute_script(
                ("return (window.pageYOffset !== undefined) ?"
                 " window.pageYOffset : (document.documentElement ||"
                 " document.body.parentNode || document.body);"))

        if new_position == old_position:
            break

    except (TimeoutException, WebDriverException) as e:
        print("Last page reached")
        break

gifs = []

for url in gifurls:
    if url not in gifs:
        gifs.append(url)

for gif in gifs:
    fileName = randomStringDigits(8) + ".gif"
    filePath = os.path.join(gifPath, fileName)
    urllib.request.urlretrieve(gif, filePath)

driver.quit()
