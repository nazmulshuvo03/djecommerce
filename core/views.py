from django.shortcuts import render

from .models import Item


def home(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "home.html", context)


def checkout(request):
    return render(request, 'checkout.html')


def product(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'product.html', context)
