from django.contrib import admin
from catalog.models import Product, Category

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name_pr", "purchase_price", "category")
    list_filter = ("category",)
    search_fields = ("name_pr", "description_pr")

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name_category")
    search_fields = ("name_category", "description_category")


