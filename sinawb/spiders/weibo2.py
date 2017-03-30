# -*- coding: utf-8 -*-
import scrapy
from sinawb.settings import USERNAME, PASSWORD
import json

class WeiboSpider(scrapy.Spider):
    name = "weibo2"
    # allowed_domains = ["m.weibo.cn"]
    start_urls = ['https://passport.weibo.cn/signin/login']

    def parse(self, response):
        cookies = {
         "_T_WM":"a60770a1810507a29624f86a7e54c214",
        "SUB":"_2A2512LrwDeRhGeRK6lAQ-SrNzj-IHXVXIsa4rDV6PUJbkdBeLRnnkW1d6EEd92xx4vb7YLn-Omk6hJ2T1w..",
        "SUHB":"0mxVjPYdKYc5xv",
        "SCF":"AkJeQiZiZ8GI0X2YCQzSCvEcXi-CMxKGdmg9eCxANky9cruR3oe8W6tb43N-wLEHhVcBx45zp50J7nFdq2W5GQg.",
        "SSOLoginState":1490864800,
        "M_WEIBOCN_PARAMS":"uicode%3D20000174",
        "H5_INDEX":"0_all",
        "H5_INDEX_TITLE":"KidGUO"
        }
        for i in range(1):
            #主页
            # yield scrapy.Request("http://m.weibo.cn/index/feed?format=cards&next_cursor=4091057656121683&page=%s"%(i+1), self.home)
            # yield scrapy.Request("http://m.weibo.cn/feed/friends?version=v4&next_cursor=4091057656121683&page=%s"% (i + 1), self.home, cookies=cookies)
            #好友圈
            yield scrapy.Request("http://m.weibo.cn/index/friends?format=cards&next_cursor=4091057656121683&page=%s" % (i + 1), self.home, cookies=cookies)

    def home(self, response):
        objs = json.loads(response.body)
        print len(objs[0]["card_group"])
        for item in objs[0]["card_group"]:
            print "The author is:" + item["mblog"]["user"]["screen_name"]
            print "The contentis:" + item["mblog"]["text"]


