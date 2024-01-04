# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from lawyers.models import *
from channels.db import database_sync_to_async

class ScraperPipeline:
    async def process_item(self, item, spider):
        await self.create_category(item['name'])
        return item

    @database_sync_to_async
    def create_category(self, name):
        return Category.objects.create(name=name)

class LawyerPipeline:
    async def process_item(self, item, spider):
        item['categories']
        await self.create_lawyer(**item)
        return item

    @database_sync_to_async
    def create_lawyer(self, **kwargs):
        keys = ['name','phone',  'email', 'office_location', 'description', 'working_hours']
        kwargs0 = {key: kwargs[key] for key in keys}
        l = Lawyer.objects.create(**kwargs0 )
        l.photo.save(kwargs['photo'][0],kwargs['photo'][1])
        l.categories.set(kwargs['categories'])
        l.save()
        return l
        
