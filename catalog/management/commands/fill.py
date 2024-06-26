from django.core.management import BaseCommand
from catalog.models import Product
from catalog.models import Category
import json

with open("data.json", "r", encoding='utf-8') as json_data:
    list_data = json.load(json_data)

class Command(BaseCommand):
    def handle(self, *args, **options):
        def get_pk_category(category_product):
            """
            Функция получает pk категории из БД
            получая на вход категорию Product из json файла сравнивает с pk Category в том же json файле
            после сравнивает имя Category из json с именами Category из БД
            :param category__product: pk продукта
            :return: pk категории из БД
            """
            for data in list_data:
                if data["model"] == "catalog.category":
                    if category_product == data['pk']:
                        for item_category in Category.objects.all():
                            if data["fields"]['name'] == item_category.name:
                                return item_category.pk

        Category.objects.all().delete()
        Product.objects.all().delete()

        for data in list_data:
            if data['model'] == 'catalog.category':
                Category.objects.create(name=data["fields"]['name'], description=data["fields"]['description'])

        for data in list_data:
            if data['model'] == 'catalog.product':
                Product.objects.create(name=data["fields"]['name'],
                                        description=data["fields"]['description'],
                                        category=Category.objects.get(pk=get_pk_category(data["fields"]["category"])),
                                        purchase_price=data["fields"]['purchase_price']
                                       )
