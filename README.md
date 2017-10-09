# Trulia Scraper
WARNING: This project is purely for non-commercial purposes. Use this code at your own risk, scraping is against Trulia's Terms and Conditions.
    A scrapy based implementation for scraping retail data from Trulia.

# Usage
Navigate to the folder location in terminal or CMD, and run the following:
```sh
scrapy crawl trulia -a state='' -a city='' [ -o {csv-filename.csv}]
```
    
Provide state and city with relevant Data.
# NOTE: The State code must be in caps and, if city name is composed of two or more words, make sure they are seperated by space and the first character is capitalized.
    
# Output Format
The scraped data will be stored in a csv file, provided the -o argument is run.

This code was written using Python 3.6.
This code was written using Scrapy 1.4.0.
