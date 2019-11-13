# Script Solution based on https://stackoverflow.com/questions/20986631/how-can-i-scroll-a-web-page-using-selenium-webdriver-in-python
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.by import By # include by implementation
import time
import csv
import os

currentDirectory = os.getcwd()
f = open(os.path.join(currentDirectory, 'ImgurPostsToCSV.csv'), 'w')  # create CSV file if it does not exist in current directory

# Requires chrome web driver path to work on using Chrome
chromeDriverLocation = './chromedriver'
# Create a new instance of the Chrome driver
driver = webdriver.Chrome(chromeDriverLocation)

# go to imgur's website
driver.get("https://imgur.com")

pages_remaining = True

SCROLL_PAUSE_TIME = 3
last_height = driver.execute_script("return document.body.scrollHeight")

with open('ImgurPostsToCSV.csv', 'w') as csvfile:
    fieldnames = ['link', 'title']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
csvfile.close()

while pages_remaining:
    try:
        # find the elements that contain the Imgur Post info
        postLinks = driver.find_elements_by_css_selector("a.Post-item")

        with open('ImgurPostsToCSV.csv', 'a') as csvfile:
            writer = csv.writer(csvfile)
            for postLink in postLinks:
                try:
                    row = [postLink.get_attribute("href"), postLink.find_element_by_xpath(".//div[@class='Post-item-title']/span").get_attribute("innerHTML")]
                    writer.writerow(row)
                except:
                    break;
        csvfile.close()

        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    except (TimeoutException, WebDriverException) as e:
        print("Last page reached")
        break

driver.quit()
