from selenium import webdriver
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.by import By # include by implementation
import time
import csv
import os

currentDirectory = os.getcwd()
f = open(os.path.join(currentDirectory, 'GitHubRepoTitlesToCSV.csv'), 'w')  # create CSV file if it does not exist in current directory

# Create a new instance of the Firefox driver
# driver = webdriver.Firefox()

# Requires chrome web driver path to work on using Chrome
chromeDriverLocation = './chromedriver'
# Create a new instance of the Chrome driver
driver = webdriver.Chrome(chromeDriverLocation)


# go to andrew's github repos
driver.get("https://github.com/andrew?tab=repositories")

pages_remaining = True

with open('GitHubRepoTitlesToCSV.csv', 'w') as csvfile:
    fieldnames = ['link', 'title']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
csvfile.close()

while pages_remaining:

    try:
        # find the elements that contain the Github Repo titles
        repoTitles = driver.find_elements_by_css_selector(".source > div > div > h3 > a")

        with open('GitHubRepoTitlesToCSV.csv', 'a') as csvfile:
            # fieldnames = ['link', 'title']
            # writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            # writer.writeheader()
            writer = csv.writer(csvfile)
            for repoTitle in repoTitles:
                print(repoTitle.get_attribute("href"))  # Get the links from Github Repo
                print(repoTitle.get_attribute("innerHTML")) # Get the titles inside of the links in Github Repo
                row = [repoTitle.get_attribute("href"), repoTitle.get_attribute("innerHTML")]
                writer.writerow(row)
        csvfile.close()

        # Select the next page button in github
        next_link = driver.find_element_by_xpath("//a[contains(@href, 'https://github.com/andrew?after=')]")
        # Click the next page button in github
        next_link.click()
        time.sleep(3)

    except (TimeoutException, WebDriverException) as e:
        print("Last page reached")
        break

driver.quit()
