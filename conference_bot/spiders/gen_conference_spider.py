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
            conference = self.driver.find_element_by_xpath(conference_xpath + "[%s]/a" % (str(i+1)))
            conference.click()
            time.sleep(1)
            
            session_xpath = "//ul[@class='talksblock']"
            
            response2 = scrapy.Selector(text=self.driver.page_source)
            
            for j in range(0, len(response2.xpath(session_xpath))):
                talks_xpath = session_xpath + "[%s]/li" % (str(j+1))
                
                for k in range(0, len(response2.xpath(talks_xpath))):
                    talk_xpath = talks_xpath + "[%s]/a" % (str(k+1))
                    talk = self.driver.find_element_by_xpath(talk_xpath)
                    talk.click()
                    time.sleep(1)
                    
                    response3 = scrapy.Selector(text=self.driver.page_source)
                
                    text_xpath = "//div[@id='primary']/p"
                    print("".join(response3.xpath(text_xpath).extract()))
                
            self.driver.get(url)
            time.sleep(3)
            
        
        self.driver.close()
        #Get search box input. 
        #search_box = self.driver.find_element_by_id("searchboxinput")
        