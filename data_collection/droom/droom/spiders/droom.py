"""
This module scraps data from droom.in a website which sells used cars. The module uses scrapy for web scraping. 
"""

import scrapy
from ..items import DroomItem

class Droom(scrapy.Spider):

	""" 
		By default it is a child class of Spider class, which uses request response module to scrape data 
		from the website and here is droom.in

		Class variables:

			name: name of the spider, which is being called while running the spider
			start_urls: The url requested at the beginning
			url: This url is going to modified and used for further request of nest pages.
			startpage: This variable is going to increase the page number after requesting a page. Means going to 
			increase for next pages.
	"""

	name = "droom"
	start_urls = ["https://droom.in/cars/used?page=1&tab=grid&bucket=car&category=car&condition=used"]
	#url = "https://droom.in/cars/used?page="+ str(Droom.startpage) + "&tab=grid&bucket=car&category=car&condition=used"
	startpage = 1

	def parse(self,response):

		""" This method is responsible for scraping data from the website and sending it to the items module

		Args:

			response: The response object from the request session, when the url is used by request

		Returns:

			Yields items (an object which have the property of car details). The items are stored as an scrapy
			Item object, which is imported from items module

		Raises:

			No errors are raised till now

		"""

		cars = DroomItem()
		container_path = "/html[1]/body[1]/div[4]/div[1]/div[1]/div[2]/div[1]/div[2]/div[3]/div[2]"
		container = response.xpath(container_path)

		for box in container:

			url = box.xpath('div/section[1]/div[1]/div[1]/div[1]/div[4]/div[1]/h4[1]/a[1]/@href').extract()
			model = box.xpath('div/section[1]/div[1]/div[1]/div[1]/div[4]/div[1]/h4[1]/@title').extract()
			price = box.xpath("div/section[1]/div[1]/div[1]/div[1]/div[4]/div[@class='price']/text()").extract()

			fuel = box.xpath('div/section[1]/div[1]/div[1]/div[1]/div[4]/div[4]/div[1]/div[1]/label[1]/text()').extract()
			location = box.xpath('div/section[1]/div[1]/div[1]/div[1]/div[4]/div[4]/div[1]/div[2]/label[1]/text()').extract()
			km_drove = box.xpath('div/section[1]/div[1]/div[1]/div[1]/div[4]/div[4]/div[1]/div[3]/label[1]/text()').extract()
			owner = box.xpath('div/section[1]/div[1]/div[1]/div[1]/div[4]/div[4]/div[1]/div[4]/label[1]/text()').extract()

			# filling the url
			if url:
				cars['url'] = url
			else:
				cars['url'] = '?'

			# filling the model
			if model:
				cars['model'] = model
			else:
				cars['model'] = '?'

			# filling the price
			if price:
				cars['price'] = price
			else:
				cars['price'] = '?'

			# filling the fuel
			if fuel:
				cars['fuel'] = fuel
			else:
				cars['fuel'] = '?'

			# filling the location
			if location:
				cars['location'] = location
			else:
				cars['location'] = '?'

			# filling the km_drove
			if km_drove:
				cars['km_drove'] = km_drove
			else:
				cars['km_drove'] = '?'

			# filling the owner
			if owner:
				cars['owner'] = owner
			else:
				cars['owner'] = '?'

			yield cars

			next_page = "https://droom.in/cars/used?page="+ str(Droom.startpage) + "&tab=grid&bucket=car&category=car&condition=used"
			if Droom.startpage <= 100000:
				Droom.startpage += 1
				yield response.follow(next_page, callback=self.parse)