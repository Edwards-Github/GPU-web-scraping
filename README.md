Newegg Product Price Scraper

This Python script allows users to scrape product prices and links from Newegg's search results. It uses Selenium and BeautifulSoup to interact with the website, extract relevant product data, and sort the results by price.

Features

Scrapes product prices and links based on a user-provided search term.

Iterates through all pages of search results on Newegg.

Outputs a sorted list of products with their prices and links.

Prerequisites

Required Libraries

Ensure the following Python libraries are installed:

bs4 (BeautifulSoup)

selenium

re

You can install these using pip:

pip install beautifulsoup4 selenium

WebDriver

Download the appropriate WebDriver for your browser (e.g., ChromeDriver for Google Chrome). Ensure the WebDriver is in your system's PATH or specify its location in the script.

ChromeDriver Downloads

Usage

Clone the repository or download the script.

Ensure you have all the prerequisites installed and set up.

Run the script:

python newegg_scraper.py

Enter the product you want to search for when prompted.

Example Input

What product do you want to search for? graphics card

Example Output

Product Name 1
$499
https://www.newegg.com/product-link
------------------------------------------
Product Name 2
$599
https://www.newegg.com/product-link
------------------------------------------

How It Works

User Input: Prompts the user to input a product name.

URL Generation: Constructs a Newegg search URL based on the input.

Page Parsing: Uses Selenium to load the webpage and BeautifulSoup to parse the HTML.

Data Extraction: Finds product names, prices, and links for all search results across pages.

Sorting: Sorts the extracted products by price in ascending order.

Output: Prints the sorted product details to the console.

Notes

The script assumes the Newegg website structure remains consistent. Changes to the site's HTML may require updates to the class names or parsing logic.

Selenium opens a browser window for scraping. Ensure your system supports this.

Potential Enhancements

Save the results to a file (e.g., CSV or JSON).

Add error handling for edge cases, such as no search results.

Use a headless browser for faster scraping without opening a browser window.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Disclaimer

This script is intended for educational purposes. Ensure compliance with Newegg's terms of service before using this script.


