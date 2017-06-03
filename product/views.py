from django.shortcuts import render, get_object_or_404

# Create your views here.
from product.models import Product


def index(request):
    return render(request, 'product/index.html', {'products': Product.objects.all()})


def get_artcile(request, id):
    data = {
        'product': get_object_or_404(Product, id=id),
    }
    return render(request, 'product/product.html', data)