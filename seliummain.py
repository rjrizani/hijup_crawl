from scrapy_selenium import SeleniumRequest
import scrapy


class HijupMainSpider(scrapy.Spider):
    name = "hijup_main"
    allowed_domains = ["hijup.com"]
    start_urls = ["https://www.hijup.com/id/products/new-arrival"]

    def start_requests(self):
        for url in self.start_urls:
            yield SeleniumRequest(url=url, callback=self.parse)

    def parse(self, response):
        # Extract product links from the page
        product_links = response.css('a.css-ao95h1::attr(href)').getall()
        for link in product_links:
            yield SeleniumRequest(
                url=response.urljoin(link),
                callback=self.parse_product,
            )

    def parse_product(self, response):
        # Identify the type of product based on URL or specific elements
        page_url = response.url

        # Example: Different handling based on URL structure
        if "skirt" in page_url:
            yield self.extract_skirt_data(response)
        elif "pants" in page_url:
            yield self.extract_pants_data(response)
        elif "blouse" in page_url:
            yield self.extract_blouse_data(response)
        elif "overall" in page_url:
            yield self.extract_overall_data(response)
        else:
            yield self.extract_default_data(response)

    def extract_skirt_data(self, response):
        """Extract data specific to skirt pages."""
        brand = response.css('div.css-1ob02yt::text').get()
        price = response.css('span.css-vurnku span::text').get()
        material = response.css('div.css-cjqqqb::text').re_first(r'Material:\s*(.*)')
        size = response.css('.css-s5rw3r::text').get()
        color = response.css('.css-cc1trw::text').get()

        return {
            'category': 'Skirt',
            'brand': brand,
            'price': price,
            'material': material,
            'size': size,
            'color': color,
            'url': response.url,
        }

    def extract_pants_data(self, response):
        """Extract data specific to pants pages."""
        brand = response.css('div.css-1ob02yt::text').get()
        price = response.css('span.css-vurnku span::text').get()
        description = response.css('div.css-cjqqqb::text').get()
        waist = response.css('.css-s5rw3r::text').re_first(r'Waist:\s*(.*)')
        length = response.css('.css-s5rw3r::text').re_first(r'Length:\s*(.*)')

        return {
            'category': 'Pants',
            'brand': brand,
            'price': price,
            'description': description,
            'waist': waist,
            'length': length,
            'url': response.url,
        }

    def extract_blouse_data(self, response):
        """Extract data specific to blouse pages."""
        brand = response.css('div.css-1ob02yt::text').get()
        price = response.css('span.css-vurnku span::text').get()
        description = response.css('div.css-cjqqqb::text').get()
        size = response.css('.css-s5rw3r::text').get()
        color = response.css('.css-cc1trw::text').get()

        return {
            'category': 'Blouse',
            'brand': brand,
            'price': price,
            'description': description,
            'size': size,
            'color': color,
            'url': response.url,
        }

    def extract_overall_data(self, response):
        """Extract data specific to overall pages."""
        brand = response.css('div.css-1ob02yt::text').get()
        price = response.css('span.css-vurnku span::text').get()
        description = response.css('div.css-cjqqqb::text').get()
        material = response.css('div.css-cjqqqb::text').re_first(r'Material:\s*(.*)')
        size = response.css('.css-s5rw3r::text').get()
        color = response.css('.css-cc1trw::text').get()

        return {
            'category': 'Overall',
            'brand': brand,
            'price': price,
            'description': description,
            'material': material,
            'size': size,
            'color': color,
            'url': response.url,
        }

    def extract_default_data(self, response):
        """Default data extraction for other pages."""
        brand = response.css('div.css-1ob02yt::text').get()
        price = response.css('span.css-vurnku span::text').get()
        description = response.css('div.css-cjqqqb::text').get()
        img_url = response.css('img.css-18aq413::attr(src)').get()

        return {
            'category': 'Other',
            'brand': brand,
            'price': price,
            'description': description,
            'img_url': img_url,
            'url': response.url,
        }
