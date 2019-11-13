from urllib import parse
from urllib import robotparser
import urllib.request
import os
import time
import requests # install requests module first

Example # 1 - Reading from a robots.txt file (Only returns partial contents from robots.txt)
AGENT_NAME = '*'
URL_BASE = 'https://en.wikipedia.org/'
parser = robotparser.RobotFileParser()
parser.set_url(parse.urljoin(URL_BASE, 'robots.txt'))
parser.read()

# Returns robots.txt content in console
print(parser)

# Example # 2 - Parser reads from url robots.txt file and then writes to a custom txt file
currentDirectory = os.getcwd()
f = open(os.path.join(currentDirectory, 'RobotsFileFromURL.txt'), 'w')

rp = robotparser.RobotFileParser()
useragent = '*'
rp.set_url("http://wikipedia.org/robots.txt")
can_fetch = rp.can_fetch(useragent, "http://wikipedia.org/")
rp.read()

# Writes contents of parser to custom file
f.write(str(rp))
f.close()

# Example # 3 - "Simple Example" revised from https://bip.weizmann.ac.il/course/python/PyMOTW/PyMOTW/docs/robotparser/index.html
# Checks if a crawler is allowed to download a page using can_fetch method
AGENT_NAME = '*'
URL_BASE = 'https://wikipedia.org/'
parser = robotparser.RobotFileParser()
parser.set_url(parse.urljoin(URL_BASE, 'robots.txt'))
parser.read()

PATHS = [
    '/',
    '/robots.txt/',
    '/wiki/admin/',
    '/wiki/Main_Page/',
    ]

for path in PATHS:
    print(parser.can_fetch(AGENT_NAME, path), path)
    url = parse.urljoin(URL_BASE, path)
    print('%6s : %s' % (parser.can_fetch(AGENT_NAME, url), url))
    print()

# Example # 4 - Returns complete robots.txt file from wikipedia.org and writes it to a file using requests module
currentDirectory = os.getcwd()
f = open(os.path.join(currentDirectory, 'RobotsFileFromURL.txt'), 'w')

response = requests.get("https://en.wikipedia.org/robots.txt")
completeRobotsTxtFile = response.text

print("robots.txt for http://www.wikipedia.org/")
print("===================================================")
print(completeRobotsTxtFile)

f.write(completeRobotsTxtFile)
f.close()
