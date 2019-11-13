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
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import keyboard
# from selenium.webdriver.common.action_chains import ActionChains

def randomStringDigits(stringLength=6):
    """Generate a random string of letters and digits """
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

# # Requires chrome web driver path to work on using Chrome
chrome_options = webdriver.ChromeOptions()
# # Includes options to disable text on Chrome browser "Chrome is being controlled by automated test software", and allows Tiktok trending pages to be accessed
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
chrome_options.add_experimental_option("useAutomationExtension", False);

caps = DesiredCapabilities().CHROME
# # Do not wait for full page load
caps["pageLoadStrategy"] = "normal"

chromeDriverLocation = './chromedriver'
# Create a new instance of the Chrome driver
driver = webdriver.Chrome(chromeDriverLocation, options=chrome_options, desired_capabilities=caps)
# driver = webdriver.Chrome(chromeDriverLocation)

# go to gfycat's trending page
driver.get("https://www.tiktok.com/trending")

pages_remaining = True

SCROLL_PAUSE_TIME = 3

# Get current directory
currentDirectory = os.getcwd()
vidPath = currentDirectory + "/videos/"

# Checks if video path exists, if not create it
if not os.path.exists(vidPath):
    print("creating directory...")
    os.mkdir(vidPath)

videoUrlLinks = []

y = 1000

driver.refresh()

# Define time_end which will run for 3 seconds (can change to any value, depends on device storage capacity)
time_end = datetime.now() + timedelta(seconds=3)
while datetime.now() < time_end:
    try:
        # Auto press page down button to scroll down page until all content has completely loaded
        keyboard.press_and_release('page down')

    except (TimeoutException, WebDriverException) as e:
        print("Last page reached")
        break

videoLinkUrls = driver.find_elements_by_css_selector("._ratio_wrapper > a")
vidUrls = []
for videoLinkUrl in videoLinkUrls:
    vidUrls.append(videoLinkUrl.get_attribute("href"))

main_window = driver.window_handles

# print(*vidUrls, sep="\n")

for url in vidUrls:
    all_windows = driver.window_handles
    new_windows = [x for x in all_windows if x != main_window][0]
    # child_window = driver.switch_to.window()
    # print(new_windows)
    driver.switch_to.window(new_windows)
    driver.execute_script("window.open('" + url +"');")
    time.sleep(1)
    # driver.close()
    # print(driver.find_element_by_css_selector("video._video_card_").get_attribute("src"))
    # time.sleep(10)
    try:
        # videoUrlLinks.append(driver.find_element_by_css_selector("video._video_card_").get_attribute("src"))
        nextUrl = driver.find_element_by_css_selector("video._video_card_").get_attribute("src")
        # driver.execute_script("window.open('" + nextUrl +"');")
        driver.get(nextUrl)
        time.sleep(1)
        # driver.close()
        try:
            videoUrlLinks.append(driver.find_element_by_css_selector("video > source").get_attribute("src"))
            driver.close()
        except:
            pass
    except:
        pass
    try:
        # videoUrlLinks.append(driver.find_element_by_css_selector("video > source").get_attribute("src"))
        nextUrl = driver.find_element_by_css_selector("video > source").get_attribute("src")
        # driver.execute_script("window.open('" + nextUrl +"');")
        driver.get(nextUrl)
        # print(nextUrl)
        time.sleep(1)
        # driver.close()
        try:
            videoUrlLinks.append(driver.find_element_by_css_selector("video > source").get_attribute("src"))
            driver.close()
        except:
            pass
    except:
        pass
    time.sleep(2)
    # driver.close()
    # time.sleep(5)

# driver.switch_to.window(main_window)

# print(*videoUrlLinks, sep="\n")

vids = []

for urlLink in videoUrlLinks:
    if urlLink not in vids:
        vids.append(urlLink)

for vid in vids:
    fileName = randomStringDigits(8) + ".mp4"
    # print(fileName + " - " + vid)
    time.sleep(1)
    filePath = os.path.join(vidPath, fileName)
    urllib.request.urlretrieve(vid, filePath)



# print(videoUrls)
time.sleep(5)
driver.quit()
