Product Search and Link Scraper

This Python script automates the process of searching for products on Newegg and extracts links to matching product listings using Selenium and BeautifulSoup.

Features
  - Accepts a user-defined search term to query Newegg's product catalog.
  - Dynamically constructs search URLs and parses results across multiple pages.
  - Utilizes BeautifulSoup to efficiently parse and navigate the HTML structure of the website.
  - Extracts and prints product links that match the search term using regular expressions.
  - Automates browser interaction to handle dynamic web content with Selenium.
  - 
Technologies Used
  - Python: Core programming language.
  - Selenium: For rendering dynamic web content and interacting with the website.
  - BeautifulSoup: For HTML parsing and data extraction.
  - re (Regular Expressions): For precise text matching and pattern extraction.
  - 
How to Use
  1. Install Selenium and BeautifulSoup libraries
      pip install selenium beautifulsoup4
  2. Download and configure ChromeDriver to match your browser version.
  3. Run the script in a Python environment.
  4. Enter a product search term when prompted.
  5. The script will print the links to all matching products.

Prerequisites
  - Python 3.x
  - Selenium and BeautifulSoup installed
  - ChromeDriver installed and in the correct path

This project demonstrates the integration of web scraping and automation tools, providing a starting point for more advanced data extraction workflows.
