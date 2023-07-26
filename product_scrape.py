#!/usr/bin/env python
# coding: utf-8

import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Configure the Chrome options
chrome_options = Options()
chrome_options.add_argument('--headless')  # To run Chrome in headless mode (without opening a window)

# Initialize the Chrome WebDriver
chrome_driver_path = '/path/to/your/chromedriver'  # Replace with the actual path to your chromedriver executable
browser = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

# Function to remove non-digit characters except the decimal point from the price string
def clean_price(price_str):
    return re.sub(r'[^\d.]', '', price_str)

# Function to extract product data
def scrape_product_data(name, min_price, max_price):
    url = f'https://www.daraz.pk/catalog/?q={name}'
    browser.get(url)

    titles = browser.find_elements(By.CLASS_NAME, 'title--wFj93')
    prices = browser.find_elements(By.CLASS_NAME, 'price--NVB62')

    for title, price in zip(titles, prices):
        title_text = title.text
        price_value = float(clean_price(price.text))
        
        if min_price <= price_value <= max_price:
            print(f'Title: {title_text}')
            print(f'Price: {price.text}\n')

# Define the products and their price ranges here
products = [
    {'name': 'Lays Salt rs 40', 'min_price': 35, 'max_price': 40},
    {'name': 'Nestle Pure Life 5L', 'min_price': 225, 'max_price': 235},
    # Add more products here as needed
]

# Scrape data for each product
for product in products:
    scrape_product_data(product['name'], product['min_price'], product['max_price'])

# Close the browser
browser.quit()
