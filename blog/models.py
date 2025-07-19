from django.db import models

class Post(models.Model):
    name = models.CharField(max_length=100, verbose_name='заголовок')
    content = models.TextField(blank=True, null=True, verbose_name='содержимое')
    image = models.ImageField(upload_to='blog/images', blank=True, null=True, verbose_name='изображение')
    created_at = models.DateField(auto_now_add=True, verbose_name='дата создания')
    is_publicated = models.BooleanField(default=True, verbose_name='признак публикации')
    views_counter = models.PositiveIntegerField(verbose_name='счетчик просмотров', default=0)


    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['name', 'created_at', 'is_publicated', 'views_counter']

    def __str__(self):
        return f'Пост {self.name} был создан {self.created_at} количество просмотров {self.views_counter}'