from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseForbidden
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from catalog.forms import ProductForm, ProductModeratorForm
from catalog.models import Product


def home(request):
    return render(request, 'home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        return HttpResponse(f'Спасибо, {name}! Ваше сообщение получено.')
    return render(request, 'contacts.html')


class ProductListView(ListView):
    model = Product


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products_list')


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products_list')

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm('catalog.can_unpublish_product'):
            return ProductModeratorForm
        if user == self.object.owner and user.has_perm('catalog.can_unpublish_product'):
            return ProductForm
        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:products_list')

    def post(self, request, *args, **kwargs):
        product_id = kwargs['pk']
        product = get_object_or_404(Product, id=product_id)

        if not request.user.has_perm('catalog.can_delete_product'):
            return HttpResponseForbidden("У вас нет прав для удаления продукта.")

        product.delete()

        return redirect('catalog:products_list')


