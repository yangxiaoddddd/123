# -*- coding: utf-8 -*-
import scrapy


class FirstSpider(scrapy.Spider):
    #爬虫文件的名称
    name = 'first'
    #允许的域名
    #allowed_domains = ['www.xxx.com']
    #起始url列表
    start_urls = ['https://www.qiushibaike.com/text/']
    #实现了数据的基本解析操作
    # def parse(self, response):
    #     div_list = response.xpath('//div[@id="content-left"]/div')
    #     for div in div_list:
    #         #author = div.xpath('./div[1]/a[2]/h2/text()')[0].extract()
    #         #如果可以保证xpath返回的列表中只有一个列表元素则可以使用extract_first(),否则必须使用extract()
    #         author = div.xpath('./div[1]/a[2]/h2/text()').extract_first()
    #         content = div.xpath('./a[1]/div/span//text()').extract()
    #         content = ''.join(content)
    #         print(author,content)

    #实现解析+持久化存储
    #1.基于终端指令的持久化存储
        # 只可以将parse方法的返回值持久化存储到本地的文本中
    #2.基于管道的持久化存储


    # 1.基于终端指令的持久化存储
    def parse(self, response):
        div_list = response.xpath('//div[@id="content-left"]/div')
        all_data = []
        for div in div_list:
            #author = div.xpath('./div[1]/a[2]/h2/text()')[0].extract()
            #如果可以保证xpath返回的列表中只有一个列表元素则可以使用extract_first(),否则必须使用extract()
            author = div.xpath('./div[1]/a[2]/h2/text()').extract_first()
            content = div.xpath('./a[1]/div/span//text()').extract()
            content = ''.join(content)

            dic = {
                'author':author,
                'content':content
            }

            all_data.append(dic)

        return all_data



