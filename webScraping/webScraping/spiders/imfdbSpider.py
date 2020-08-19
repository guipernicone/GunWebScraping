import scrapy

from ..items import WebscrapingItem
class ImfdbSpider(scrapy.Spider):
    base_url = "http://www.imfdb.org";
    name = "imfdb";
    start_urls = ["http://www.imfdb.org/wiki/File:Glock173rdGen.jpg"]

    def parse(self, response):
        links = response.xpath("//li[@id='mw-imagepage-linkstoimage-ns0']//a/@href")
        
        for link in links:
            url = link.get()
            # print(url)
            absolute_urls = self.base_url + url;
            yield scrapy.Request(absolute_urls, callback=self.parseImg)
    
    def parseImg(self, response):
        imgs = response.xpath("//img[@class='thumbimage']/@src")

        item = WebscrapingItem()
        item['image_urls'] = []
        for img in imgs:
            src = img.get()
            item['image_urls'].append(self.base_url + src);

        yield item

       