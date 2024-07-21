from django.shortcuts import render, get_object_or_404

from catalog.models import Product


# Create your views here.
def home(request):
    product_list = Product.objects.all()
    contex = {
        'object_list' : product_list
    }
    return render(request, 'home.html',contex)


def contacts(request):
    if request. method == 'POST':
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        massage = request.POST.get("massage")
        print(f'{name} ({phone}): {massage}')
    return render(request, 'contacts.html')


def  products(request, pk):
    product = get_object_or_404(Product, pk=pk)
    contex = {
        'product': product
    }
    return render(request, 'product.html',contex)
