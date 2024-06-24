from django.core.management import BaseCommand
from catalog.models import Product
from catalog.models import Category

class Command(BaseCommand):
    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()
