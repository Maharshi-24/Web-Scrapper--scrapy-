import scrapy
import pandas as pd

class WebScrapeSpider(scrapy.Spider):
    name = "web_scrape"
    start_urls = []

    def __init__(self, url):
        self.start_urls = [url]

    def parse(self, response):
        # Scrape details from the webpage
        title = response.css('title::text').get()
        headers = response.css('h1,h2,h3,h4,h5,h6::text').getall()
        paragraphs = response.css('p::text').getall()

        # Create a dictionary to store the scraped data
        data = {
            'Title': [title],
            'Headers': headers,
            'Paragraphs': paragraphs
        }

        # Convert the dictionary to a Pandas DataFrame
        df = pd.DataFrame(data)

        # Return the DataFrame
        return df