# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import re

class HijupPipeline:
    def process_item(self, item, spider):
        item['title'] = self.get_product_name_from_url(item['title']) if item['title'] else None
        x = item['price_RP'][1] if len(item['price_RP'][1]) > 3 else item['price_RP'][0]
        item['price_RP'] = self.clean_price(x)
        #item['price'] = self.clean_price(item['price'])
        item['availability'] = item['availability'].strip() if item['availability'] else "Sold Out"
        return item
        
    def clean_price(self,price):
        # Menghapus semua karakter kecuali angka
        return int(re.sub(r'\D', '', price))
    
    def get_product_name_from_url(self,url):
        match = re.search(r'/(\d+)-(.+)$', url)
        return match.group(2).replace('-', ' ') if match else None
        
