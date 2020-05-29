# -*- coding: utf-8 -*-
import scrapy


class ItemlinkSpider(scrapy.Spider):
    name = 'itemlink'
    start_urls = ['https://www.bsnsports.com//']

    def parse(self, response):
        link = {}
        linkxp = '((//ul[@id="pronav"]/li)/div/ul/li[not(@class="parent-info")])//a[not(@class="parent")]/@href'
        linklist = response.xpath(linkxp).getall()
        for i in linklist:
            link["link"]=i
            yield link
        
        nextpage = response.urljoin('/equipment/sports/football')
        yield scrapy.Request(nextpage, callback=self.parsedata)

    def parsedata(self,response):
        link2 = {}
        linklistfball = response.xpath('//body[@class=" catalog-category-view categorypath-equipment-sports-football category-football"]//div[@class="land-container"]/a/@href').getall()
        for i in linklistfball:
            link2["link"]=i
            yield link2

