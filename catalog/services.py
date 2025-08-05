from .models import Product, Category

class ProductService:

    @staticmethod
    def get_products_in_category(category_id):
        products_in_category = Product.objects.filter(category_id=category_id)
        if not products_in_category.exists():
            return None
        return products_in_category