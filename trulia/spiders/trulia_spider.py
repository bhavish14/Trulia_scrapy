import scrapy
from scrapy.http import Request
from trulia.items import TruliaItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spider import Rule

class trulia_spider(scrapy.Spider):
    name = "trulia"

    def __init__(self, region = '', city = '', *args, **kwargs):
        super(trulia_spider, self).__init__(*args, **kwargs)
        base_url = "https://www.trulia.com/"
        city = city.replace(' ', '_')
        url = base_url + '/' + region + '/' + city
        self.start_urls = [url]

    def start_requests(self):
        allowed_domains = ["https://www.trulia.com/"]
        for item in self.start_urls:
            yield scrapy.Request(url=item, callback=self.parse)

    def parse(self, response):
        outer_wrapper = response.xpath('//li[@class="smlCol12 lrgCol8"]')
        for item in outer_wrapper:
            Item = {}
            Item['retail_price'] = item.xpath(
                './/span[@class="cardPrice h5 man pan typeEmphasize noWrap typeTruncate"]/text()').extract()
            if item.xpath('.//li[@data-auto-test="beds"]/text()'):
                Item['bedrooms'] = item.xpath('.//li[@data-auto-test="beds"]/text()').extract()
            Item['area'] = item.xpath('.//li[@data-auto-test="sqft"]/text()').extract()
            if item.xpath('.//li[@data-auto-test="baths"]/text()'):
                Item['barthrooms'] = item.xpath('.//li[@data-auto-test="baths"]/text()').extract()
            Item['region'] = item.xpath('.//span[@itemprop="addressRegion"]/text()').extract()
            Item['postal_code'] = item.xpath('.//span[@itemprop="postalCode"]/text()').extract()
            Item['latitude'] = item.xpath('.//meta[@itemprop="latitude"]/@content').extract()
            Item['longitude'] = item.xpath('.//meta[@itemprop="longitude"]/@content').extract()
            Item['street_address'] = item.xpath('.//span[@itemprop="streetAddress"]/text()').extract()
            yield Item

        next_url = response.xpath('//a[@aria-label="Next page"]/@href').extract_first()
        print(next_url)
        yield Request(response.urljoin(next_url), callback=self.parse)
