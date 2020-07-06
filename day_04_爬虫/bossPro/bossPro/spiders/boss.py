# -*- coding: utf-8 -*-
import scrapy

from bossPro.items import BossproItem
class BossSpider(scrapy.Spider):
    name = 'boss'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.zhipin.com/job_detail/?query=python%E7%88%AC%E8%99%AB&scity=101010100&industry=&position=']

    url = 'https://www.zhipin.com/c101010100/?query=python爬虫&page=%d&ka=page-2'
    page = 1
    #解析+管道持久化存储
    def parse(self, response):
        li_list = response.xpath('//div[@class="job-list"]/ul/li')
        for li in li_list:
            job_name = li.xpath('.//div[@class="info-primary"]/h3/a/div/text()').extract_first()
            salary = li.xpath('.//div[@class="info-primary"]/h3/a/span/text()').extract_first()
            company = li.xpath('.//div[@class="company-text"]/h3/a/text()').extract_first()

            #实例化一个item对象
            item = BossproItem()
            #将解析到的数据全部封装到item对象中
            item['job_name'] = job_name
            item['salary'] = salary
            item['company'] = company

            #将item提交给管道
            yield item

        if self.page <= 3:
            print('if 执行!!!')
            self.page += 1
            new_url = format(self.url%self.page)
            print(new_url)
            #手动请求发送
            yield scrapy.Request(url=new_url,callback=self.parse)