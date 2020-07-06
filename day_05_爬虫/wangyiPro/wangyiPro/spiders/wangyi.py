# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver


'''
在scrapy中使用selenium的编码流程:
    1.在spider的构造方法中创建一个浏览器对象(作为当前spider的一个属性)
    2.重写spider的一个方法closed(self,spider),在该方法中执行浏览器关闭的操作
    3.在下载中间件的process_response方法中,通过spider参数获取浏览器对象
    4.在中间件的process_response中定制基于浏览器自动化的操作代码(获取动态加载出来的页面源码数据)
    5.实例化一个响应对象,且将page_source返回的页面源码封装到该对象中
    6.返回该新的响应对象
'''

class WangyiSpider(scrapy.Spider):
    name = 'wangyi'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://war.163.com/']
    def __init__(self):
        self.bro = webdriver.Chrome(executable_path=r'C:\Users\Administrator\Desktop\爬虫+数据\day_03_爬虫\chromedriver.exe')
    def parse(self, response):
        div_list = response.xpath('//div[@class="data_row news_article clearfix "]')
        for div in div_list:
            title = div.xpath('.//div[@class="news_title"]/h3/a/text()').extract_first()
            print(title)
    def closed(self,spider):
        print('关闭浏览器对象!')
        self.bro.quit()

