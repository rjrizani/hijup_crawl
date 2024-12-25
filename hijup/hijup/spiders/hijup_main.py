import scrapy
from scrapy.spiders.crawl import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Response


class HijupMainSpider(CrawlSpider):
    name = "hijup_main"
    allowed_domains = ["hijup.com"]
    #https://www.hijup.com/id/products/new-arrival
    #start_urls = ["https://www.hijup.com/id/skirt/141065-aurel-skirt-rok-basic-katun-putih"]
    start_urls = ["https://www.hijup.com/id/products/new-arrival"]

    rules = [
        Rule(
             LinkExtractor(
                #allow=(r"id/(skirt|pants|dress|jacket|jumpsuit|coat|shirt)/[0-9]+.*"), 
                allow=(r"id/skirt/[0-9]+.*"),
                  # Tambahkan kategori lain jika diperlukan
            ),
            callback="parse", follow=True,
        ),
        Rule(
            LinkExtractor(
                #?product_search%5Bpage%5D=
                allow=(r"id/products/new-arrival"),  # Matches pagination links
            ),
            follow=True,  # Follow pagination links
            #
            callback="parse",
        )
           
        ]

    def parse(self, response: Response):
        self.logger.info(f"Scraping URL: {response.url}")
        title = response.css("div.css-1us5m20 ::text").get()
        brand = response.css('div.css-1ob02yt::text').get()
        price = response.css('span.css-vurnku span::text').get()
        all_desc = response.css('div.css-cjqqqb::text').getall()
        description = all_desc[0] if len(all_desc) > 0 else None
        material = all_desc[1] if len(all_desc) > 1 else None
        size = response.css('.css-s5rw3r::text').get()
        color_elements = response.css('.css-cc1trw::text').getall()
        color = color_elements[1] if len(color_elements) > 1 else None
        url = response.url
        img_url = response.css('img.css-18aq413::attr(src)').get()

        yield {
            'title': title,
            'brand': brand,
            'price': price,
            'description': description, 
            'material': material,   
            'size': size,
            'color': color,
            'url': url, 
            'img_url': img_url  
        }

