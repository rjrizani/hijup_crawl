# MarketPlace Scraper: Extracting Data from [hijup.com](https://www.hijup.com/id/products/new-arrival)

This project demonstrates how to use Scrapy to scrape marketplace websites.

## Getting Started

**Prerequisites:**

- Python 3.x (https://www.python.org/downloads/)
- Scrapy (https://scrapy.org/) - `pip install scrapy`

**Project Setup:**

1. Clone the repository:

   ```bash
   https://github.com/rjrizani/hijup_crawl.git

2. (Optional) Create a virtual environment
  
3. Install project dependencies
   ```
   pip install -r requirements.txt

## Running the Scraper
   ```bash
   cd hijup/hijup
   scrapy crawl hijup_main
   

**Saving to CSV**
    scrapy crawl hijup_main -o output.csv
