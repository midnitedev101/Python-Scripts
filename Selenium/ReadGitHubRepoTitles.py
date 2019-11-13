from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.by import By # include by implementation


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

for repoTitle in repoTitles:
    print(repoTitle.get_attribute("href"))  # Get the links from Github Repo
    print(repoTitle.get_attribute("innerHTML")) # Get the titles inside of the links in Github Repo

try:
    # we have to wait for the page to refresh, the last thing that seems to be updated are the anchor links
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.source > div > div > h3 > a')))


    # You should see "midnitedev101 / Repositories · GitHub"
    print(driver.title)

finally:
    driver.quit()
