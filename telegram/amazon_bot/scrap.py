import requests
from bs4 import BeautifulSoup
import time 
import sys
import urllib3 

class ProductDetails:
	def __init__(self, url, username):
		self.url = url
		self.username = username

	def get_content(self):
		# Target URL
		target_url = self.url
		
		# Headers of the browser which is acting as a user. 
		# Change according to the browser
		headers = {
			"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
		}

		# Make a call witn the spcified url 
		amazon = requests.get(target_url, headers = headers)

		# Scrap the data from the called url
		soup = BeautifulSoup(amazon.content, 'html.parser')

		# Find the extracted detail fields from the page 
		self.product_name = soup.find(id = "productTitle").get_text().strip()
		self.product_price =  soup.find(id = "priceblock_ourprice").get_text()[1:].strip().replace(',','')