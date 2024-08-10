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
    fields = ('name','description', 'preview', 'category', 'purchase_price')
    success_url = reverse_lazy('product:list')

    def form_valid(self, form):
        new_mat = form.save()
        new_mat.slug = slugify(new_mat.title)
        new_mat.save()
        return super().form_valid(form)

class ProductUpdateView(UpdateView):
    model = Product
    fields = ('name', 'description', 'preview', 'category', 'purchase_price')

    def form_valid(self, form):
        new_mat = form.save()
        new_mat.slug = slugify(new_mat.title)
        new_mat.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('editor:view', args=[self.kwargs.get('pk')])
class ProductDeleteView(DeleteView):
    model = Product


    success_url = reverse_lazy('editor:list')