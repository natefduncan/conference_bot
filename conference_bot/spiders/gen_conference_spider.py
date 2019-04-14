#General packages
import scrapy
import os
import time
from pathlib import Path

path = Path(os.path.dirname(os.path.realpath(__file__)))
path = path / "Data"
os.chdir(str(path))

#Selenium packages
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

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
            print("IN 1")
            time.sleep(3)
            
            conference = self.driver.find_element_by_xpath(conference_xpath + "[%s]/a" % (str(i+1)))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", conference)
            conference.click()
            time.sleep(1)
            
            session_xpath = ("//ul[@class='talksblock']")
            
            response = scrapy.Selector(text=self.driver.page_source)
            for j in range(0, len(response.xpath(session_xpath))):
                print("IN 2")
                talks_xpath = session_xpath + "[%s]/li" % (str(j+1))
                time.sleep(2)
                
                for k in range(0, len(response.xpath(talks_xpath))):
                    print("IN 3")
                    talk_xpath = talks_xpath + "[%s]/a[contains(@onclick, 'getTalk')]/div[contains(@class, 'talktitle')]" % (str(k+1))
                    talk = self.driver.find_element_by_xpath(talk_xpath)
                    self.driver.execute_script("arguments[0].scrollIntoView(true);", talk)
                    talk.click()
                    time.sleep(3)
                    
                    response = scrapy.Selector(text=self.driver.page_source)
                
                    text_xpath = "//div[@id='primary']/p/text()"
                    
                    file_name = response.xpath("//div[@id='talklabel']/a/text()").extract()[0]
                    file_name += response.xpath("//div[@id='talklabel']/text()").extract()[0]
                    
                    text = u"".join(response.xpath(text_xpath).extract()).encode("utf-8")
                    with open(file_name + ".txt", "w+") as file:
                        file.write(text)
            
            print("NEW URL")
            self.driver.get(url)
            time.sleep(3)
            
        self.driver.close()
        #Get search box input. 
        #search_box = self.driver.find_element_by_id("searchboxinput")
        