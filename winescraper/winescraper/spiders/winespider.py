import scrapy
from sqlalchemy import false
from websockets import Origin
from winescraper.items import WineItem
import dateutil.parser as dparser

class WineSpider(scrapy.Spider):
    name = 'Wine_1'
    basic_url = 'https://www.weinauktion.de/index.php?site=auktion&cat='
    # Note: Auktionen müssen Typ Internet sein, sonst kein Abschlussgebot vergeben
    start_index = 399           # latest site available 26-01-2019
    # end_index = 501             
    end_index = 454             # Ab 454 kommt Zuschlag Feld für finalen Preis hinzu
    start_urls = []
    for idx in range(start_index, end_index):
        start_urls.extend([basic_url + str(idx)])

    def parse(self, response):
        wine_item = WineItem()

        page = response.css('li.active')
        auction = response.css('span.btn-sm::text').get()
        if "Internet" in auction:           # Filter out Präsenzauktionen
            yield {'Auction': auction, 'Page': page.css('a::text').get().replace(' ', '')}

            for products in response.css('li.ajax_block_product'):
                wine_item['auctiondate'] = dparser.parse(auction, fuzzy=True)
                wine_item['name'] = products.css('h3.weinname::text').get()
                origin = products.css('div.weinurs')
                wine_item['origin'] = origin.css('span::text').get()
                description = products.css('div.bewertung')
                wine_item['description'] = description.css('span::text').get()
                state = products.css('div.zustand')
                wine_item['state'] = state.css('span::text').get()
                packaging = products.css('div.verpackung')
                wine_item['packaging'] = packaging.css('span::text').get() 
                price = products.css('div.col-xs-4.col-md-4.col-lg-4')
                wine_item['price'] = price.css('span::text').get().replace('\xa0EUR', '')#
                min_max_price = products.css('div.col-xs-4.col-md-4.col-lg-4')
                min_max_price = min_max_price.css('div:nth-child(n+3)::text').get().replace('EUR ', '')
                wine_item['minimum_price'] = float(min_max_price.split('-')[0]) 
                wine_item['maximum_price'] = float(min_max_price.split('-')[1]) 

                yield wine_item

            try:
                next_page = response.css('a.pagebar-link.pagebar-navlink.pagebar-navlink-next').attrib['href']
                if next_page is not None:
                    yield response.follow(next_page, callback=self.parse)
            except Exception as e:
                print("Error thrown: " + e)
                pass