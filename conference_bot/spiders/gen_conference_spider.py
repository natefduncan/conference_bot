#General packages
import scrapy
import os

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
            yield scrapy.Request(url=url, callback=self.parse)
    
    def __init__(self):
        self.driver = webdriver.Firefox()
        
    def parse(self, response):
        self.driver.get(response.url)
        
        response = scrapy.Selector(text=self.driver.page_source)
        
        with open("test.txt", "w+") as file: 
            file.write(self.driver.page_source)
        
        #Get search box input. 
        #search_box = self.driver.find_element_by_id("searchboxinput")
        