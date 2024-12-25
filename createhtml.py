import scrapy

class MySpider(scrapy.Spider):
    name = 'myspider'
    start_urls = ['https://www.hijup.com/id/skirt/141065-aurel-skirt-rok-basic-katun-putih']

    def parse(self, response):
        with open('page.html', 'w') as f:
            f.write(response.text)