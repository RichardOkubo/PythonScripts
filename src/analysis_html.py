from pprint import pprint

import requests
from bs4 import BeautifulSoup

url = "https://stackoverflow.com/questions/56860183/how-to-find-allid-from-a-div-with-beautiful-soup-in-python/56860413"

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

ids = [tag['id'] for tag in soup.select('div[id]')]

#results = soup.findAll("div", {"valign" : "top"})

tags = soup.find_all(id="notify-container")

pprint(tags)
