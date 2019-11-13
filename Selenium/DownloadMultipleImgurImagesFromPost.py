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

def randomStringDigits(stringLength=6):
    """Generate a random string of letters and digits """
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

# Requires chrome web driver path to work on using Chrome
chromeDriverLocation = './chromedriver'
# Create a new instance of the Chrome driver
driver = webdriver.Chrome(chromeDriverLocation)

# driver.implicitly_wait(30) # seconds

# go to imgur's website
driver.get("https://imgur.com/gallery/OWLLHjI")

SCROLL_PAUSE_TIME = 3
last_height = driver.execute_script("return document.body.scrollHeight")

# Get current directory
currentDirectory = os.getcwd()
imagesPath = currentDirectory + "/image/"

# Checks if image path exists, if not create it
if not os.path.exists(imagesPath):
    print("creating directory...")
    os.mkdir(imagesPath)

imageurls = []

pages_remaining = True

y = 1000

while pages_remaining:
    try:
        old_position = driver.execute_script(
                ("return (window.pageYOffset !== undefined) ?"
                 " window.pageYOffset : (document.documentElement ||"
                 " document.body.parentNode || document.body);"))
        # print("old_position:", old_position)

        images = driver.find_elements_by_tag_name('img')
        moreLink = driver.find_elements_by_css_selector("a.post-loadall")   # Checks if there is a load more button on the post

        for image in images:
            if image.get_attribute("src") is not None:
                imageurls.append(image.get_attribute("src"))

        if len(moreLink) > 0:   # If loadmore link is found, then allow automation to click it
            moreLink[0].click()
        # else:
        #     print("moreLink not found")

        driver.execute_script("window.scrollTo(0, "+str(y)+")")
        y += 1000
        time.sleep(1)

        new_position = driver.execute_script(
                ("return (window.pageYOffset !== undefined) ?"
                 " window.pageYOffset : (document.documentElement ||"
                 " document.body.parentNode || document.body);"))
        # print("new_position:", new_position)

        if new_position == old_position:
            break

    except (TimeoutException, WebDriverException) as e:
        print("Last page reached")
        break

# print(imageurls)

imgs = []

for url in imageurls:
    if url not in imgs:
        imgs.append(url)

for img in imgs:
    fileName = randomStringDigits(8) + ".png"
    filePath = os.path.join(imagesPath, fileName)
    urllib.request.urlretrieve(img, filePath)

driver.quit()
