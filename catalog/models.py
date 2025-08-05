from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование категории')
    description = models.TextField(blank=True, null=True, verbose_name='описание категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование продукта')
    description = models.TextField(blank=True, null=True, verbose_name='описание продукта')
    image = models.ImageField(upload_to='catalog/image_pr', blank=True, null=True, verbose_name='вид продукта')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name='категория', null=True, blank=True,
                                 related_name='products')
    price = models.FloatField(verbose_name='цена покупки')
    created_at = models.DateField(auto_now_add=True, verbose_name='дата создания')
    updated_at = models.DateField(auto_now=True, verbose_name='дата последнего изменения')
    views_counter = models.PositiveIntegerField(verbose_name='счетчик просмотров', default=0)
    status_publication = models.BooleanField(verbose_name='статус публикации', default=False, null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='владелец', null=True, blank=True,
                              related_name='products')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name', 'category', 'created_at']
        permissions = [
            ('can_unpublish_product', 'Can unpublish product'),
            ('can_delete_product', 'Can delete product')
        ]

    def __str__(self):
        return f'Продукт {self.name} категории {self.category} был создан {self.created_at}'
