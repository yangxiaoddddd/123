# -*- coding: utf-8 -*-
import scrapy


class PostSpider(scrapy.Spider):
    name = 'post'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://fanyi.baidu.com/sug']

    def start_requests(self):
        data = {
            'kw':'dog'
        }
        for url in self.start_urls:
            yield scrapy.FormRequest(url=url,formdata=data,callback=self.parse)

    def parse(self, response):
        print(response.text)
