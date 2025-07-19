import os

from django.forms import ModelForm
from .models import Product
from django.core.exceptions import ValidationError
from constants import spam

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'price']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control',
                                                 'placeholder': 'Введите наименование'})
        self.fields['description'].widget.attrs.update({'class': 'form-control',
                                                 'placeholder': 'Добавьте описание'})
        self.fields['image'].widget.attrs.update({'class': 'form-control', })
        self.fields['category'].widget.attrs.update({'class': 'form-control',})
        self.fields['price'].widget.attrs.update({'class': 'form-control',})


    def clean_name(self):
        name = self.cleaned_data.get('name')
        for elem in spam:
            if elem.upper() in name.upper():
                self.add_error('name', f'name не может содержать слово {elem}')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        for elem in spam:
            if elem.upper() in description.upper():
                self.add_error('description', f'description не может содержать слово {elem}')
        return description


    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise ValidationError('Цена покупки не может быть отрицательной')
        return price

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            if image.size > 5 * 1024 * 1024:
                raise ValidationError("Размер файла не должен превышать 5MB")
            extension = os.path.splitext(image.name)[1].lower()
            if extension not in ['.jpeg', '.jpg', 'png']:
                raise ValidationError("Файл должен быть в формате jpeg, jpg или png")
        return image
