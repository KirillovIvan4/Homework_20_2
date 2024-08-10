from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.models import Product
from catalog.forms import ProductForm


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'


def contacts(request):
    if request. method == 'POST':
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        massage = request.POST.get("massage")
        print(f'{name} ({phone}): {massage}')
    return render(request, 'catalog/contacts.html')

class ProducDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:list')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:list')

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:list')
