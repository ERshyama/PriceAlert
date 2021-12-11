from utils import selenium_scraper

prices = selenium_scraper()

for crypto, price in prices.items():
    print('Price of ' + crypto + ' is ' + price)
