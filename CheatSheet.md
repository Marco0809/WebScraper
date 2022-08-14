# Cheatsheet Scrapy

## Start Scrapy spiders
On cmd, type:

```scrapy crawl quotes```


## Invoke debugger
    if "page" in response.url:
        from scrapy.shell import inspect_response
        inspect_response(response, self) }

## Response attributes
```
response
response.body
response.headers
response.url
response.status
response.flags
response.request
response.ip_address
```
## Response CSS
```
response.css('p')
response.css('div')
```
## Response XPath
```
response.xpath('//a')
response.xpath('//div')
```

## Auktionshaus Koppe
https://www.weinauktion.de/index.php?site=auktion&cat=456
# Get Title/Name 
```
products.css('a.vip::text').getall()
```
# Get Winetype
```
names = products.css('div.weinurs')
names.css('span::text').getall()
```
# Get Bewertung
```
bewertung = products.css('div.bewertung')
bewertung.css('span::text').getall()
```
# Get Zustand
```
zustand = products.css('div.zustand')
zustand.css('span::text').getall()
```
# Get Verpackung
```
verpackung = products.css('div.verpackung')
verpackung.css('span::text').getall() 
```
#### Vorsicht bei leeren Feldern

# Get aktuelles Gebot
```
gebote = products.css('div.col-xs-4')
gebote_aktuell = gebote.css('b')
gebote_aktuell.css('span::text').getall()
gebote_aktuell.css('span::text').get().replace('\xa0EUR', '') //Replace single element
```

# Get Preisempfehlung
```
gebote = products.css('div.col-xs-4')
gebote.css('div::text').getall() // nur jeder zweite Eintrag
```