from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

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

class ProductCreateView(CreateView):
    model = Product
    fields = ('title', 'preview', 'body')
    success_url = reverse_lazy('product:list')
class ProductUpdateView(UpdateView):
    model = Product

class ProductDeleteView(DeleteView):
    model = Product