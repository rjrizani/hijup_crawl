# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class HijupPipeline:
    def process_item(self, item, spider):
        item['price'] = item['price'][1] if len(item['price'][1]) > 3 else item['price'][0]
        #item['price'] = self.extract_numeric_price(item['price'])
        item['availability'] = item['availability'].strip() if item['availability'] else "Sold Out"
        return item
    

    def extract_numeric_price(self, price):
        import re
        match = re.search(r'\d+(?:\.\d+)?', price)
        if match:
            return match.group().replace('.', '')
        else:
            return None
        
