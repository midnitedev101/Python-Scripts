# Script Solution based on https://stackoverflow.com/questions/20986631/how-can-i-scroll-a-web-page-using-selenium-webdriver-in-python
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.by import By # include by implementation
import time

# Requires chrome web driver path to work on using Chrome
chromeDriverLocation = './chromedriver'
# Create a new instance of the Chrome driver
driver = webdriver.Chrome(chromeDriverLocation)

# go to imgur's website
driver.get("https://imgur.com")

pages_remaining = True

SCROLL_PAUSE_TIME = 3
last_height = driver.execute_script("return document.body.scrollHeight")

while pages_remaining:
    try:
        # find the elements that contain the Imgur Post info
        postLinks = driver.find_elements_by_css_selector("a.Post-item")

        for postLink in postLinks:
            # Retrieves link for the imgur post
            print(postLink.get_attribute("href"))

            # Try/Except clause required for accessing child element of Post-item-title because errors will occur if time runs out before child element is retrieved
            # Retrieves title of the imgur post
            try:
                print(postLink.find_element_by_xpath(".//div[@class='Post-item-title']/span").get_attribute("innerHTML"))
            except:
                break;

            print()

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
