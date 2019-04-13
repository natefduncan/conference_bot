#General packages
import scrapy
import os
import time

path = os.path.dirname(os.path.realpath(__file__))
os.chdir(path)

#Selenium packages
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class google(scrapy.Spider):
    name = "gen_conference"
    
    def start_requests(self):
        urls = ["https://scriptures.byu.edu/#::g"]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, meta={'url' : url})
    
    def __init__(self):
        self.driver = webdriver.Firefox()
        
    def parse(self, response):
        url = response.meta['url']
        self.driver.get(url)
        
        time.sleep(3)
        
        response = scrapy.Selector(text=self.driver.page_source)
        
        conference_xpath = ("//ul[@class='conflist']/li")
        print("TRYING")
        
        for i in response.xpath(conference_xpath):
            print(i)
            print(i.xpath("a/text()").extract())
        
        #Get search box input. 
        #search_box = self.driver.find_element_by_id("searchboxinput")
        