# -*- coding: utf-8 -*-
import scrapy


class ItemlinkSpider(scrapy.Spider):
    name = 'items'
    start_urls = ['https://www.bsnsports.com/bsn-sports-phenom-short-sleeve-t-shirt']

    def parse(self, response):
        name = (response.xpath('//div[@class="product-main-info"]/div/h1/text()').get()).strip()
        sku = response.xpath('//div[@class="product-main-info"]/div[@id="product_addition_info"]/p/text()').get()
        colorlist = response.xpath('//ul[@id="color_products"]/li/input[3]/@value').getall()
        colors = []
        for i in colorlist:
            colors.append(i.strip())
        size = response.xpath('//div[@id="size_products"]/div/ul/li/label[1]/text()').getall()
        price = response.xpath('//div[@class="price-addToCart-section"]//span/span[@class="price"]/text()').get()
        details = response.xpath('//div[@class="box-description"]/p/text()').get()
        addikeys = response.xpath('//table[@id="product-attribute-specs-table"]/tbody/tr/th/text()').getall()
        addival = response.xpath('//table[@id="product-attribute-specs-table"]/tbody/tr/td/text()').getall()
        addivalues = []
        for i in addival:
            addivalues.append(" ".join(i.split()))
        additional = {}
        for i in range(len(addikeys)):
            additional.update({addikeys[i]:addivalues[i]})
        yield {
            "name":name,
            "sku":sku,
            "colors":colors,
            "size":size,
            "price":price,
            "details":details,
            "additional":additional
        }

        
