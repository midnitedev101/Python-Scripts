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
f = open(os.path.join(currentDirectory, 'YTVideoInfoToCSV.csv'), 'w')  # create CSV file if it does not exist in current directory

# Requires chrome web driver path to work on using Chrome
chromeDriverLocation = './chromedriver'
# Create a new instance of the Chrome driver
driver = webdriver.Chrome(chromeDriverLocation)

# go to youtube's trending page
driver.get("https://www.youtube.com/feed/trending")

pages_remaining = True

SCROLL_PAUSE_TIME = 3
last_height = driver.execute_script("return document.body.scrollHeight")

with open('YTVideoInfoToCSV.csv', 'w') as csvfile:
    fieldnames = ['link', 'title']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
csvfile.close()

while pages_remaining:
    try:
        # find the elements that contain the Imgur Post info
        postLinks = driver.find_elements_by_css_selector("ytd-video-renderer")
        # postLinks = driver.find_elements_by_tag_name("ytd-video-renderer")

        # for postLink in postLinks:
        #     # print(postLink)
        #     # postLinkUrl = postLink.find_element_by_css_selector("a.thumbnail")
        #     # print(postLinkUrl)
        #     # print(postLink.get_attribute("href"))
        #     postLinkUrl = postLink.find_element_by_xpath(".//a[@id='thumbnail']").get_attribute("href")
        #     postLinkTitle = postLink.find_element_by_xpath(".//a[@id='video-title']").get_attribute("innerHTML")
        #     print(postLinkUrl)
        #     print(postLinkTitle)
        #     print()

        with open('YTVideoInfoToCSV.csv', 'a') as csvfile:
            writer = csv.writer(csvfile)
            for postLink in postLinks:
                try:
                    postLinkUrl = postLink.find_element_by_xpath(".//a[@id='thumbnail']").get_attribute("href")
                    postLinkTitle = postLink.find_element_by_xpath(".//a[@id='video-title']").get_attribute("innerHTML")
                    row = [postLinkUrl, postLinkTitle]
                    writer.writerow(row)
                except:
                    break
        csvfile.close()

        try:
            # we have to wait for the page to refresh, the last thing that seems to be updated are the anchor links
            WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a#thumbnail')))

            print()

        except (TimeoutException, WebDriverException) as e:
            print("No results retrieved")
            break

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
