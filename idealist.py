#									Scraping Idealista - Real Estate Website
#												By Devi Nanda
#
# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
import json
import datetime


class IdealistSpider(scrapy.Spider):
    name = 'idealist'
    base_url = 'https://www.idealista.com/buscar/venta-oficinas/'
    headers = {
	   	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
    }
    #current page counter
    current_page = 2
    #postcodes list
    postcodes = []

    #init constructor
    def __init__(self):
    	content = ''

    	#open postcodes.txt file
    	with open('postcodes.txt', 'r', encoding = 'utf-8') as f:
    		for line in f.read():
    			content += line
    	#parse content
    	self.postcodes = list(filter(None,content.split('\n')))
    
    #crawlers entry point
    def start_requests(self):
    	#reset current page
    	self.current_page = 2

    	#loop over postcodes
    	for postcode in self.postcodes:
    		#generate next postcode url
    		next_postcode = self.base_url + str(postcode) + '/'
    		print(next_postcode)

