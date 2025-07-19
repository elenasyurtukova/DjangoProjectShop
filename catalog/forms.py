from django.forms import ModelForm
from .models import Product
from django.core.exceptions import ValidationError

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
        self.fields['image'].widget.attrs.update({'class': 'form-control',
                                                        'placeholder': 'Загрузите изображение'})
        self.fields['category'].widget.attrs.update({'class': 'form-control',})
        self.fields['image'].widget.attrs.update({'class': 'form-control',})


    def clean(self):
        spam = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')
        for elem in spam:
            if elem.upper() in name.upper():
                self.add_error('name', f'name не может содержать слово {elem}')
            if elem.upper() in description.upper():
                self.add_error('description', f'description не может содержать слово {elem}')


    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise ValidationError('Цена покупки не может быть отрицательной')
        return price