from django.shortcuts import render
from .models import Product


def index(request):
    items = Product.objects.all()
    return render(request, 'myapp/index.html', {'items': items})


def index_item(request, my_id):
    item = Product.objects.get(id=my_id)
    data = {
        'item': item,
    }
    return render(request, 'myapp/details.html', data)