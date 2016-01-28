__author__ = 'juming.wang'

import scrapy
from LearnScrapy.items import DmozItem
class DmozSpider(scrapy.Spider):

    name = "dmoz"

    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    """
        Scrapy creates scrapy.Request objects for each URL in the start_urls attribute of the Spider, and assigns them the parse method of the spider as their callback function.
        These Requests are scheduled, then executed, and scrapy.http.Response objects are returned and then fed back to the spider, through the parse() method.
    """

    def parse(self, response):

        # TODO:old code
        # filename = response.url.split("/")[-2] + '.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)

        # use item and xpath
        for sel in response.xpath('//ul/li'):
            item = DmozItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['desc'] = sel.xpath('text()').extract()
            yield item

    """
        Selectors have four basic methods (click on the method to see the complete API documentation):
        xpath(): returns a list of selectors, each of which represents the nodes selected by the xpath expression given as argument.
        css(): returns a list of selectors, each of which represents the nodes selected by the CSS expression given as argument.
        extract(): returns a unicode string with the selected data.
        re(): returns a list of unicode strings extracted by applying the regular expression given as argument.
    """