from selenium import webdriver
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.by import By # include by implementation
import time


# Create a new instance of the Firefox driver
# driver = webdriver.Firefox()

# Requires chrome web driver path to work on using Chrome
chromeDriverLocation = './chromedriver'
# Create a new instance of the Chrome driver
driver = webdriver.Chrome(chromeDriverLocation)


# go to andrew's github repos
driver.get("https://github.com/andrew?tab=repositories")

pages_remaining = True

while pages_remaining:

    try:
        # find the elements that contain the Github Repo titles
        repoTitles = driver.find_elements_by_css_selector(".source > div > div > h3 > a")

        for repoTitle in repoTitles:
            print(repoTitle.get_attribute("href"))  # Get the links from Github Repo
            print(repoTitle.get_attribute("innerHTML")) # Get the titles inside of the links in Github Repo

        try:
            # we have to wait for the page to refresh, the last thing that seems to be updated are the anchor links
            WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.source > div > div > h3 > a')))


            # You should see "midnitedev101 / Repositories · GitHub"
            print(driver.title)

        except (TimeoutException, WebDriverException) as e:
            print("No results retrieved")
            break

        # Select the next page button in github
        next_link = driver.find_element_by_xpath("//a[contains(@href, 'https://github.com/andrew?after=')]")
        # Click the next page button in github
        next_link.click()
        time.sleep(3)

    except (TimeoutException, WebDriverException) as e:
        print("Last page reached")
        break

driver.quit()
