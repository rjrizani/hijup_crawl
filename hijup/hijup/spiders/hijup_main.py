import scrapy
from scrapy.spiders.crawl import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Response
from datetime import datetime


class HijupMainSpider(CrawlSpider):
    name = "hijup_main"
    allowed_domains = ["hijup.com"]
    #start_urls = ["https://www.hijup.com/id/skirt/141065-aurel-skirt-rok-basic-katun-putih"]
    start_urls = ["https://www.hijup.com/id/products/new-arrival"]

    rules = [
        Rule(
            LinkExtractor(
                #?product_search%5Bpage%5D=
                allow=[r"product_search%5Bpage%5D=",
                       #r"skirt",
                       #r"pants",
                       r'tunik'
                   
                ], 
            ),
            follow=True, callback="parse",
        )   
           
        ]

    def parse(self, response: Response):
        self.logger.info(f"Scraping URL: {response.url}")
        title = response.url
        brand = response.css('div.css-1ob02yt::text').get()
        price_RP= response.css('span.css-vurnku span::text').getall()
       
        all_desc = response.css('div.css-cjqqqb::text').getall()
        description = all_desc[0] if len(all_desc) > 0 else None
        material = all_desc[1] if len(all_desc) > 1 else None
        size = response.css('.css-s5rw3r::text').get()
        color_elements = response.css('.css-cc1trw::text').getall()
        color = color_elements[1] if len(color_elements) > 1 else None
        availability = response.css("div.css-1odyx6k span::text").get()   
        url = response.url
        img_url = response.css('img.css-18aq413::attr(src)').get()
        scraped_at =  datetime.now().date()

        if availability is not None and availability not in 'Sold Out':
            yield {
                'title': title,
                'brand': brand,
                'price_RP': price_RP,
                'description': description, 
                'material': material,   
                'size': size,
                'color': color,
                'availability': availability,
                'url': url, 
                'img_url': img_url,
                'scraped_at': scraped_at
            }
        else:
            pass