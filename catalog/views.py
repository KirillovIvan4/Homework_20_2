from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html')


def contacts(request):
    if request. method == 'POST':
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        massage = request.POST.get("massage")
        print(f'{name} ({phone}): {massage}')
    return render(request, 'contacts.html')


def product(request):
    return render(request, 'product.html')
