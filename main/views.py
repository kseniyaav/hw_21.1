from django.shortcuts import render
from main.models import Product


def index(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list,
    }
    return render(request, 'main/product.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name}, {phone}: {message}')
    return render(request, 'main/contacts.html')


def product(request, pk):
    context = {
        'object': Product.objects.get(pk=pk),
    }
    return render(request, 'main/product.html', context)
