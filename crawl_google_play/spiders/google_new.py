# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from crawl_google_play.items import CrawlGooglePlayItem
from urllib.parse import urlparse
# from parsel import selector

class GoogleSpider(CrawlSpider):
    name = 'google'
    allowed_domains = ['play.google.com','privacygrade.org']
    start_urls = ["https://play.google.com/store/apps/","http://privacygrade.org/apps",]
                  # 'https://play.google.com/store/apps/details?id=com.viber.voip']

    rules = (
        Rule(LinkExtractor(allow=('http://privacygrade.org/apps',)), follow=True),
        Rule(LinkExtractor(allow=('/store/apps',), deny=('/store/apps/details', )), follow=True),
        Rule(LinkExtractor(allow=("/store/apps/details", )), follow=True, callback='parse_link'),
    )


    def parse_start_url(self, response):
        return scrapy.Request(url=response.url,callback=self.parse)

    def parse_link(self,response):
        items = []
        for title in response.xpath('/html'):
            item = CrawlGooglePlayItem()
            item["Link"] = title.xpath('head/link[5]/@href').extract_first()
            item["Item_name"] = title.xpath('//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div[1]/div/c-wiz[1]/c-wiz[1]/div/div[2]/div/div[1]/c-wiz[1]/h1/span/text()').extract_first()
            item["Updated"] = title.xpath('//div[contains(text(), "Updated")]/following-sibling::span[1]/div/span/text()').extract_first()
            item["Author"] = title.xpath('//div[contains(text(), "Offered By")]/following-sibling::span[1]/div/span/text()').extract_first()
            item["Filesize"] = title.xpath('//div[contains(text(), "Size")]/following-sibling::span[1]/div/span/text()').extract_first()
            item["Downloads"] = title.xpath('//div[contains(text(), "Installs")]/following-sibling::span[1]/div/span/text()').extract_first()
            item["Version"] = title.xpath('//div[contains(text(), "Current Version")]/following-sibling::span[1]/div/span/text()').extract_first()
            item["Compatibility"] = title.xpath('//div[contains(text(), "Requires Android")]/following-sibling::span[1]/div/span/text()').extract_first()
            # item["Content_rating"] = title.xpath('//div[contains(text(), "Content Rating")]/following-sibling::span[1]/div/span/text()').extract_first()
            # item["Author_link"] = title.xpath('//*[@class="dev-link"]/@href').extract_first()
            # item["Author_link_test"] = titles.xpath('//*[@class="content contains-text-link"]/a/@href').extract_first()
            item["Genre"] = title.xpath('//a[@itemprop="genre"]/text()').extract_first()
            item["Price"] = title.xpath('//meta[@itemprop="price"]/@content').extract_first()
            item["Rating_value"] = title.xpath('//div[@class="K9wGie"]/div/text()').extract_first()
            item["Review_number"] = title.xpath('//span[@class="EymY4b"]/span[2]/text()').extract_first()
            item["Description"] = title.xpath('//meta[@name="description"]/@content').extract_first()
            # item["IAP"] = title.xpath('//*[@class="inapp-msg"]/text()').extract_first()
            # item["Developer_badge"] = title.xpath('//*[@class="badge-title"]//text()').extract_first()
            # item["Physical_address"] = title.xpath('//*[@class="content physical-address"]/text()').extract_first()
            # item["Video_URL"] = title.xpath('//*[@class="play-action-container"]/@data-video-url').extract_first()
            # item["Developer_ID"] = title.xpath('//*[@itemprop="author"]/a/@href').extract_first()

            yield item
            # print(item)

