# Trulia Scraper
A scrapy based implementation for scraping retail data from Trulia.
Note: This project is purely for non-commercial purposes. Use this code at your own risk, scraping is against Trulia's Terms and Conditions.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Installing

A step by step series of examples on how to get a development env running

```
cd <your-path>/Trulia_scrapy
scrapy crawl trulia -a state=<state-name> -a city=<city-name> [ -o {csv-filename.csv}]
```

NOTE: The State code must be in caps and, if city name is composed of two or more words, make sure they are seperated by space and the first character is capitalized.
    
#### Output Format
The scraped data will be stored in a csv file, provided the -o argument is run.

This code was written using Python 3.6.
This code was written using Scrapy 1.4.0.

## Authors

* **Bhavish Khanna narayanan** - *Initial work* - [bhavish14](https://github.com/bhavish14)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


