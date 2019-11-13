from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.by import By # include by implementation
import csv
import os

# currentDirectory = os.getcwd()
# f = open(os.path.join(currentDirectory, 'GitHubRepoTitlesToCSV.csv'), 'w')
# csv_file_writer = csv.writer(f, delimiter=",", quoting=csv.QUOTE_ALL, quotechar="'")
# csv_file_writer.writerow(list_data)

# Create a new instance of the Firefox driver
# driver = webdriver.Firefox()

# Requires chrome web driver path to work on using Chrome
chromeDriverLocation = './chromedriver'
# Create a new instance of the Chrome driver
driver = webdriver.Chrome(chromeDriverLocation)


# go to midnitedev101's github repos
driver.get("https://github.com/midnitedev101?tab=repositories")

# the page is ajaxy so the title is originally this:
print(driver.title)

# find the elements that contain the Github Repo titles
repoTitles = driver.find_elements_by_css_selector(".source > div > div > h3 > a")

# open csv
# with open('GitHubRepoTitlesToCSV.csv') as csvFile:
#     writer = csv.writer(csvFile)
#     row_count = sum(1 for line in csvFile)
#     print(row_count)
# csvFile.close()

with open('GitHubRepoTitlesToCSV.csv', 'a') as appendToCsvFile:
    writer = csv.writer(appendToCsvFile)
    for repoTitle in repoTitles:
        print(repoTitle.get_attribute("href"))  # Get the links from Github Repo
        print(repoTitle.get_attribute("innerHTML")) # Get the titles inside of the links in Github Repo
        row = [repoTitle.get_attribute("href"), repoTitle.get_attribute("innerHTML")]
        writer.writerow(row)
appendToCsvFile.close()

try:
    # we have to wait for the page to refresh, the last thing that seems to be updated are the anchor links
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.source > div > div > h3 > a')))


    # You should see "midnitedev101 / Repositories · GitHub"
    print(driver.title)
finally:
    driver.quit()
