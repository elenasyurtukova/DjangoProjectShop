from django.db import models


class Category(models.Model):
    name_category = models.CharField(max_length=100, verbose_name='наименование категории')
    description_category = models.TextField(blank=True, null=True, verbose_name='описание категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name_category']

    def __str__(self):
        return self.name_сategory


class Product(models.Model):
    name_pr = models.CharField(max_length=100, verbose_name='наименование продукта')
    description_pr = models.TextField(blank=True, null=True, verbose_name='описание продукта')
    image_pr = models.ImageField(upload_to='catalog.image_pr', blank=True, null=True, verbose_name='вид продукта')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    purchase_price = models.FloatField(verbose_name='цена покупки')
    created_at = models.DateField(verbose_name='дата создания')
    updated_at = models.DateField(verbose_name='дата последнего изменения')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name_pr', 'category', 'created_at']

    def __str__(self):
        return f'Продукт {self.name_pr} категории {self.category} был создан {self.created_at}'
