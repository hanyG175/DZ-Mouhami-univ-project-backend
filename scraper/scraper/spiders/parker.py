import scrapy
from scraper.items import *
import json
import requests,os
from django.core.files import File
from lawyers.models import Category
from asgiref.sync import sync_to_async
from channels.db import database_sync_to_async
from django.core.files.storage import default_storage
from django.utils.text import slugify

class ParkerSpider(scrapy.Spider):
    name = "parker"
    allowed_domains = ["avocatalgerien.com"]
    start_urls = ["https://avocatalgerien.com/categories/"]
    
    
    def parse(self, response):
        # Extract category links and follow them
        for href in response.css('li.maincat a::attr(href)'):
            yield response.follow(href, self.parse_category)
            
    def parse_category(self, response):
        # Extract item links and follow them
        for href in response.css('h2.entry-title a ::attr(href)'):
            yield response.follow(href, self.parse_item)
            
        next_page_url = response.css('a.next::attr(href)').get()
        if next_page_url is not None:
            yield response.follow(next_page_url, self.parse_category)


    async def parse_item(self, response):
        # Extract item details
        photo= response.css('img.attachment-medium::attr(src)').get()
        
        photo_name = os.path.basename(photo) if photo is not None else ""
        print(photo_name)

# Construct the path using os.path.join
        res = requests.get(photo)
        
        if res.status_code == 200 :
            with open(f"C:/Users/LENOVO/Code/GLPROJECT/backend/media/photos/{photo_name}", 'wb') as f:
                f.write(res.content)
            
            selected_categories = await self.get_categories(response)
            selected_categories = await sync_to_async(set)(selected_categories)
            info= {
                'name': response.css('h1.entry-title a::text').get(),
                'photo': (photo_name, File(open(f"C:/Users/LENOVO/Code/GLPROJECT/backend/media/photos/{photo_name}", 'rb')) ),       
                'email': response.css('li#listing-email a::text').get(),
                'office_location': response.css('li.address::text').get(),
                'categories':  set(selected_categories),
                'description': response.css('section#overview p::text').getall(),
                'working_hours': response.css('section#hours p::text').get(),
            } 
            
            request = requests.post("https://avocatalgerien.com/wp-admin/admin-ajax.php" ,data={'action': 'reveal_phone','post_id': response.css('strong.reveal::attr(data-post_id)').get()})
            data = json.loads(request.text)
            info['phone']=data['response']
    
        
        yield LawyerItem(**info)
        
    @database_sync_to_async
    def get_categories(self, response):
    # Synchronous Django ORM operation
    # Replace this with your actual code to get categories
        categories=  response.css('p.listing-cat a::text').getall()
        return list(map(lambda x: Category.objects.get(name=x).id ,Category.objects.filter(name__in=categories).values_list('name', flat=True)))
