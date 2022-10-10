import scrapy
from sqlalchemy import false

class WineSpider(scrapy.Spider):
    name = 'Wine'
    basic_url = 'https://www.weinauktion.de/index.php?site=auktion&cat='
    # Note: Auktionen müssen Typ Internet sein, sonst kein Abschlussgebot vergeben
    start_index = 399           # latest site available 26-01-2019
    start_index = 400           # letzte verfügbare Internetauktionen
    start_urls = ['https://www.weinauktion.de/index.php?site=auktion&cat=' + str(start_index)]

    def parse(self, response):
        page = response.css('li.active')
        
        yield {'Auction': response.css('span.btn-sm::text').get(), 'Page': page.css('a::text').get().replace(' ', '')}

        for products in response.css('li.ajax_block_product'):
            winename = products.css('a.vip::text').get()
            winetype = products.css('div.weinurs')
            winetype = winetype.css('span::text').get()
            valuation = products.css('div.bewertung')
            valuation = valuation.css('span::text').get()
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
                'winetype': winetype,
                'valuation': valuation,
                'state': state,
                'packaging': packaging,
                'current_bids': current_bids,
                'price_recommendation': price_recommendation}

            yield wine_dict
        next_page = response.css('a.pagebar-link.pagebar-navlink.pagebar-navlink-next').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)