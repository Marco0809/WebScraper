import scrapy
from sqlalchemy import false
from websockets import Origin

class WineSpider(scrapy.Spider):
    name = 'Wine'
    basic_url = 'https://www.weinauktion.de/index.php?site=auktion&cat='
    # Note: Auktionen müssen Typ Internet sein, sonst kein Abschlussgebot vergeben
    start_index = 399           # latest site available 26-01-2019
    current_index = 402           # letzte verfügbare Internetauktionen
    end_index = 453             # Ab 454 kommt Zuschlag Feld für finalen Preis hinzu
    start_index = 453           # latest site available 26-01-2019
    current_index = 402           # letzte verfügbare Internetauktionen
    end_index = 501             # Ab 454 kommt Zuschlag Feld für finalen Preis hinzu
    start_urls = []
    for idx in range(start_index, end_index):
        start_urls.extend([basic_url + str(idx)])

    def parse(self, response):
        page = response.css('li.active')
        auction = response.css('span.btn-sm::text').get()
        if "Internet" in auction:           # Filter out Präsenzauktionen
            yield {'Auction': auction, 'Page': page.css('a::text').get().replace(' ', '')}

            for products in response.css('li.ajax_block_product'):
                winename = products.css('h3.weinname::text').get()
                origin = products.css('div.weinurs')
                origin = origin.css('span::text').get()
                description = products.css('div.bewertung')
                description = description.css('span::text').get()
                state = products.css('div.zustand')
                state = state.css('span::text').get()
                packaging = products.css('div.verpackung')
                packaging = packaging.css('span::text').get() 
                bids = products.css('div.col-xs-4')
                current_bids = bids.css('b')
                current_bids = current_bids.css('span::text').get().replace('\xa0EUR', '') # Only for 
                price_recommendation = products.css('div.col-xs-4') ## TODO: Nur jeden zweiten Eintrag
                price_recommendation = price_recommendation.css('div::text').get()

                wine_dict = {#'Auction': auction_main_titel,
                    'name': winename,
                    'origin': origin,
                    'description': description,
                    'state': state,
                    'packaging': packaging,
                    'current_bids': current_bids,
                    'price_recommendation': price_recommendation}

                yield wine_dict
            next_page = response.css('a.pagebar-link.pagebar-navlink.pagebar-navlink-next').attrib['href']
            if next_page is not None:
                yield response.follow(next_page, callback=self.parse)