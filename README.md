# GPU Web Scraping with Python

## Project Overview
This project is a Python-based web scraper designed to search for GPUs (or other products) on **Newegg**. By automating searches and extracting product details like price and link, this script provides a simple way to compare prices across multiple pages. It’s a practical project for exploring web scraping and automation using **BeautifulSoup** and **Selenium**.

## Features
  - Allows users to input a search term for any product.
  - Scrapes product details, including name, price, and URL, from Newegg.
  - Sorts and displays results in ascending order of price for easy comparison.

## Requirements
To run this project, you'll need:
  - Python 3.6 or later
  - Google Chrome installed
  - ChromeDriver compatible with your Chrome version
  - Selenium and BeautifulSoup libraries

## Installation
1. Clone this repository to your local machine:
```
https://github.com/Edwards-Github/GPU-web-scraping.git
```
2. Install the required Python libraries:
  ```
  pip install selenium beautifulsoup4
  ```
3. Download and place the appropriate `chromedriver.exe` in the project directory
  ```
  https://googlechromelabs.github.io/chrome-for-testing/
  ```

## Usage
1. Run the script
  ```
  python gpu_web_scraping.py
  ```
2. Enter the name of the product you want to search for (e.g., "GeForce RTX 4090").
3. The script will:
  - Open Newegg’s website and search for the specified product.
  - Scrape product details (name, price, and link) across all pages.
  - Display the sorted results in the terminal.

## How It Works
  - Selenium WebDriver: Opens the browser and navigates through search results.
  - BeautifulSoup: Parses HTML to extract product information.
  - Regex Matching: Identifies product names that match the search term.
  - Sorting Mechanism: Organizes scraped items by price for easier comparison.

## Example Output
```
ASUS TUF Gaming GeForce RTX 4090 Gaming Graphics Card (PCIe 4.0, 24GB GDDR6X, HDMI 2.1a, DisplayPort 1.4a) TUF-RTX4090-24G-GAMING
$3399
https://www.newegg.com/asus-geforce-rtx-4090-tuf-rtx4090-24g-gaming/p/N82E16814126596
------------------------------------------------------------------------------------------------------------------------
MSI Ventus GeForce RTX 4090 24GB GDDR6X PCI Express 4.0 Video Card RTX 4090 VENTUS 3X E 24G OC
$3399
https://www.newegg.com/msi-video-card-rtx-4090-ventus-3x-e-24g-oc-nvidia-geforce-rtx-4090-24gb-gddr6x/p/N82E16814137842
------------------------------------------------------------------------------------------------------------------------
ABS Vortex-X Aqua High Performance Gaming PC – Intel i9 13900K - GeForce RTX 4090 - 32GB DDR5 5600MHz - 2TB M.2 NVMe SSD – VXA139KF490
$3599
https://www.newegg.com/abs-vxa139k490-vortex-x-aqua/p/N82E16883360371C
------------------------------------------------------------------------------------------------------------------------
```
