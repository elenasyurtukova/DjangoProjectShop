from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Add test products to the database'

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()


        category, _ = Category.objects.get_or_create(name='соки', description='охлаждающие напитки')

        products = [
            {"name": "сок вишневый сады придонья 0,2",
             "description": "соки",
             "image": "",
             "category": category,
             "price": 30.0,
             "created_at": "2025-06-29",
             "updated_at": "2025-06-29"},
            {"name": "сок яблочный сады придонья 0,2",
             "description": "соки",
             "image": "",
             "category": category,
             "price": 30.0,
             "created_at": "2025-06-29",
             "updated_at": "2025-06-29"},
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added product: {product.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Product already exists: {product.name}'))
