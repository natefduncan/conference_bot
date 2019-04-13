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
        
        for i in range(0, len(response.xpath(conference_xpath))):
            conference = driver.find_element_by_xpath(conference_xpath + "/a[%s]" % (str(i+1))
            conference.click()
            time.sleep(1)
            
            talk_xpath = "//ul[@class='talksblock']/li"
            
            response2 = scrapy.Selector(text=self.driver.page_source)
            response2.xpath(talk_xpath)
            
            for j in range(0, len(response2.xpath(talk_xpath))):
                print(response2.xpath(talk_xpath).extract()[j])
                
            self.driver.get(url)
            time.sleep(3)
            
        
        self.driver.close()
        #Get search box input. 
        #search_box = self.driver.find_element_by_id("searchboxinput")
        