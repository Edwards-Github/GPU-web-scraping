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

items_found = {}

# Iterate over every page
for page in range(1, page_total + 1):
	# get url matching user's search
	url = f"https://www.newegg.com/p/pl?d={search_term}&page={page}"
	# open driver with url & parse html on webpage
	dr.get(url)
	
	doc = BeautifulSoup(dr.page_source, "html.parser")

	div = doc.find(class_="item-cells-wrap border-cells short-video-box items-list-view is-list")
	if div == None:
		continue
	else:
		items = div.find_all(string=re.compile(search_term))

	for item in items:
		parent = item.parent
		link = None
		if parent.name != "a":
			continue

		link = parent['href']
		next_parent = item.find_parent(class_="item-container")
		price = next_parent.find(class_="price-current").strong

		if price == None:
			continue
		else:
			try:
				int(price.string.replace(",", ""))
				items_found[item] = {"price": price.string.replace(",", ""), "link": link}
			except:
				pass

sorted_items = sorted(items_found.items(), key=lambda x: x[1]['price'])

for item in sorted_items:
	print(item[0])
	print(f"${item[1]['price']}")
	print(item[1]['link'])
	print("------------------------------------------")
