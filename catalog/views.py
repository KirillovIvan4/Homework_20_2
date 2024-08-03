from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from catalog.models import Product


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
    template_name = 'catalog/product.html'

