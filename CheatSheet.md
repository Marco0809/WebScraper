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

