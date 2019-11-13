from selenium import webdriver
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.by import By # include by implementation
import urllib.request
import random
import string
import os

def randomStringDigits(stringLength=6):
    """Generate a random string of letters and digits """
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

# Requires chrome web driver path to work on using Chrome
chromeDriverLocation = './chromedriver'
# Create a new instance of the Chrome driver
driver = webdriver.Chrome(chromeDriverLocation)

# go to imgur's website
driver.get("https://imgur.com/gallery/m2DJ0wr")

# Get current directory
currentDirectory = os.getcwd()
imagesPath = currentDirectory + "/image/"

# Checks if image path exists, if not create it
if not os.path.exists(imagesPath):
    print("creating directory...")
    os.mkdir(imagesPath)

# Sets file name using random digits and numbers from randomStringDigits function
fileName = randomStringDigits(8) + ".jpg"

# Join current images path and image file to create the complete path for the downloaded image
filePath = os.path.join(imagesPath, fileName)

# Find single image from Imgur Post using its default structure
if driver.find_elements(By.CSS_SELECTOR, ".post-image-container > div > img"):
    img = driver.find_element_by_css_selector(".post-image-container > div > img").get_attribute("src")
# Find single image from Imgur Post using another structure (includes anchor link)
elif driver.find_elements(By.CSS_SELECTOR, ".post-image-container > div > a > img"):
    img = driver.find_element_by_css_selector(".post-image-container > div > a > img").get_attribute("src")
else:
    print("Web Element is not found")
    driver.quit()

urllib.request.urlretrieve(img, filePath)


driver.quit()
