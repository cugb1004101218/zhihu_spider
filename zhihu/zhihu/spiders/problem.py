#!/usr/bin/env python
# encoding: utf-8

from scrapy.spider import Spider
from scrapy.selector import Selector
from zhihu.items import *
from scrapy.http.request import Request

class ProblemSpider(Spider):
    name = "problem"
    allowed_domains = ["m.zhihu.com"]
    start_urls = [
        "https://m.zhihu.com/question/37135753"
    ]
    def start_requests(self):
        cookies = {
            '_ga': 'GA1.2.1708906577.1432855516',
            '_xsrf':'2b02d2be72455fd6f96e89dc375c8685',
            '_za':'609116a6-e5f6-4041-a540-ccb3b6469ead',
            'q_c1':'6699bf91950849f685fe026449ce52a8|1449407256000|1400340161000',
            '__utmt':'1',
            'cap_id':"NzhkMGY3YmI4MTY5NDJkYjhmODE2YmRmMTgyZjc4ZmQ=|1449408083|544bb2736bbc001d09295605f6cb8199a5ae2724",
            'z_c0':"QUFEQWFJTWZBQUFYQUFBQVlRSlZUWHpEaTFhbUN2X3RnQjRLNUZfT1lldm81YkNaams3TnBnPT0=|1449408124|22e73eb7e23b01a602cf168c0e296eba5bdc56d6",
            'unlock_ticket':"QUFEQWFJTWZBQUFYQUFBQVlRSlZUWVE5WkZZNUk4RTZXNE5MOC1Ja0RSdjlVM2NHck9WMTRBPT0=|1449408124|0eb3b43847c8f1a49c31bccd67f3e3b895572b92",
            '__utma':'51854390.1708906577.1432855516.1448509276.1449407260.57',
            '__utmb':'51854390.18.10.1449407260',
            '__utmc':'51854390',
            '__utmz':'51854390.1448007583.54.34.utmcsr=baidu|utmccn=(organic)|utmcmd=organic',
            '__utmv':'51854390.110-1|2=registration_date=20131021=1^3=entry_date=20131021=1',
        }
        for url in self.start_urls:
            yield Request(url, cookies=cookies)

    def parse(self, response):
        answer_list = response.selector.xpath('//div[@id="zh-question-answer-wrap"]/div[@class="zm-item-answer  zm-item-expanded"]')
        for ans in answer_list:
            print "fuck========================"
            ans_head = ans.xpath('div[@class="answer-head"]')
            author_info = ans_head.xpath('div[@class="zm-item-answer-author-info"]')
            name = author_info.xpath('a[@class="author-link"]/text()').extract()
            author_title = author_info.xpath('span[@class="bio"]/text()').extract()
            content = ans.xpath('div/div[@class="zm-editable-content clearfix"]/*')
            try:
                for c in content:
                    image = c.xpath('img/@src').extract()
                    txt = c.xpath('text()').extract()
                    if len(image) > 0:
                        print '\n'.join(image)
                    print '\n'.join(txt)
                print name[0], author_title[0]
            except:
                pass
