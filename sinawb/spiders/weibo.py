# -*- coding: utf-8 -*-
import scrapy
from sinawb.settings import USERNAME, PASSWORD
import json

class WeiboSpider(scrapy.Spider):
    name = "weibo"
    # allowed_domains = ["m.weibo.cn"]
    start_urls = ['https://passport.weibo.cn/signin/login']

    def parse(self, response):
        return scrapy.FormRequest.from_response(response,
                formdata = {"username":USERNAME, "password":PASSWORD},
                method = "POST",
                url = "https://passport.weibo.cn/sso/login",
                callback = self.after_login)

    def after_login(self, response):
        for i in range(5):
            # yield scrapy.Request("http://m.weibo.cn/index/feed?format=cards&next_cursor=4091057656121683&page=%s"%(i+1), self.home)
            yield scrapy.Request(
                "http://m.weibo.cn/feed/friends?version=v4&next_cursor=4091057656121683&page=%s"% (i + 1), self.home)

    def home(self, response):
        objs = json.loads(response.body)
        print len(objs[0]["card_group"])
        for item in objs[0]["card_group"]:
            print item["mblog"]["text"]


