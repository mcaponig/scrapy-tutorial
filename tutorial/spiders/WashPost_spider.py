import scrapy

import sys
sys.path.append('/Users/matthewcaponigro/Documents/Analytics-Code/tutorial/tutorial') # this path address will need refactored if script is moved
from items import NewsItem

class WashPostSpider(scrapy.Spider):
    name = "WashPost"
    allowed_domains = ["washingtonpost.com"]
    start_urls = [
        "http://www.washingtonpost.com/politics/high-court-to-decide-whether-to-take-up-major-abortion-case/2015/06/22/dd2da650-18ae-11e5-bed8-1093ee58dad0_story.html"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        item = NewsItem()
        item['title'] = sel.xpath #fill this in
        item['url'] = start_urls
        
        for sel in response.xpath('//p'):
            print sel
