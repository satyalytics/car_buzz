"""
	This module aims to collect data from cars24 website.
"""

import scrapy
from ..items import Cars24Item

class Cars24(scrapy.Spider):

	""" 
		It is a child class of Spider. It works to extract data from cars24
	"""

	name = "cars24"
	start_urls=['https://www.cars24.com/buy-used-car?sort=P&storeCityId=7323']

	def parse(self,response):
		
		"""
			collect the data from the http response object

			Args:
				response: The response object
			Returns:
				Yields the item object, where details of car is taken
		"""

		table_path = "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]"
		table = response.xpath(table_path)

		for i in table:
			item = Cars24Item()

			model = i.xpath('div/div[1]/div[2]/a[1]/div[1]/div[1]/h5[1]/text()').extract()
			price = i.xpath('div/div[1]/div[2]/a[1]/div[2]/div[1]/h3[1]/text()').extract()
			# url = i.xpath('').extract()
			km_drove = i.xpath('div/div[1]/div[2]/a[1]/div[2]/div[2]/p[1]/span[1]/text()').extract()
			fuel = i.xpath('div/div[1]/div[2]/a[1]/div[2]/div[2]/p[1]/span[2]/span[1]/text()').extract()
			owner = i.xpath('div/div[1]/div[2]/a[1]/div[2]/div[2]/p[1]/span[3]/text()').extract()

			# if url:
			# 	item['url'] = url
			# else:
			# 	item['url'] = '?'

			if model:
				item['model'] = model
			else:
				item['model'] = '?'

			if price:
				item['price'] = price
			else:
				item['price'] = '?'

			if fuel:
				item['fuel'] = fuel
			else:
				item['fuel'] = '?'

			if km_drove:
				item['km_drove'] = km_drove
			else:
				item['km_drove'] = '?'

			if owner:
				item['owner'] = owner
			else:
				item['owner'] = '?'

			yield item