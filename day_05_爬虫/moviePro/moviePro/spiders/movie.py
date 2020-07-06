# -*- coding: utf-8 -*-
import scrapy
from moviePro.items import MovieproItem

class MovieSpider(scrapy.Spider):
    name = 'movie'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.4567tv.tv/frim/index1.html']
    #解析详情页中的数据
    def parse_detail(self,response):
        #response.meta返回接收到的meta字典
        item = response.meta['item']
        actor = response.xpath('/html/body/div[1]/div/div/div/div[2]/p[3]/a/text()').extract_first()
        item['actor'] = actor

        yield item

    def parse(self, response):
        li_list = response.xpath('//li[@class="col-md-6 col-sm-4 col-xs-3"]')
        for li in li_list:
            item = MovieproItem()
            name = li.xpath('./div/a/@title').extract_first()
            detail_url = 'https://www.4567tv.tv'+li.xpath('./div/a/@href').extract_first()
            item['name'] = name
            #meta参数:请求传参.meta字典就会传递给回调函数的response参数
            yield scrapy.Request(url=detail_url,callback=self.parse_detail,meta={'item':item})