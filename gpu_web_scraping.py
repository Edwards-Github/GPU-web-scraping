from bs4 import BeautifulSoup
from selenium import webdriver
import re

# create driver
dr = webdriver.Chrome()

# get input from user
search_term = input("What product do you want to search for? ")

# get url matching user's search
url = f"https://www.newegg.com/p/pl?d={search_term}&N=4131"

# open driver with url & parse html on webpage
dr.get(url)
doc = BeautifulSoup(dr.page_source, "html.parser")

# find class for page number
page_text = doc.find("span", {"class": "list-tool-pagination-text"})
# isolate the page number
pages = str(page_text).split("/")[-3]
page_total = int(pages.split(">")[-1][:-1])

# Iterate over every page
for page in range(1, page_total + 1):
	# get url matching user's search
	url = f"https://www.newegg.com/p/pl?d={search_term}&page={page}"
	# open driver with url & parse html on webpage
	dr.get(url)
	
	doc = BeautifulSoup(dr.page_source, "html.parser")

	div = doc.find(class_="item-cells-wrap border-cells short-video-box items-list-view is-list")
	items = div.find_all(text=re.compile(search_term))

	for item in items:
		parent = item.parent
		link = None
		if parent.name == "a":
			link = parent['href']

		print(link)
