from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import contacts, products_list

app_name = CatalogConfig.name

urlpatterns = [
    path('contacts/', contacts, name='contacts'),
    path('', products_list)
]
