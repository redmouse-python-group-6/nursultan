from django.shortcuts import render, get_object_or_404

# Create your views here.
# from comments.forms import CommentsForm
from comments.models import Comment
from product.models import Product, Category



def index(request):
    category_parent = Category.objects.filter(category_parent=None)
    category_chaild = [i for i in Category.objects.all() if i.category_parent in category_parent]
    data = {
        'products': Product.objects.all(),
        'categorys': category_parent,
        'category_chaild': category_chaild,
    }
    return render(request, 'product/index.html', data)


def get_product(request, id):
    category_parent = Category.objects.filter(category_parent=None)
    category_chaild = [i for i in Category.objects.all() if i.category_parent in category_parent]
    data = {
        'product': get_object_or_404(Product, id=id),
        'categorys': category_parent,
        'category_chaild': category_chaild,
        'comments': Comment.objects.filter(comment_product_id=id),
    }
    return render(request, 'product/product.html', data)


def get_category(request, id):

    category = Category.objects.get(id=id)
    category_parent = Category.objects.filter(category_parent=None)
    category_chaild = [i for i in Category.objects.all() if i.category_parent in category_parent]
    data = {

        'products': Product.objects.filter(product_categry_id=category.id),
        'category': category,
        'categorys': category_parent,
        'category_chaild': category_chaild,
    }
    return render(request, 'product/category.html', data)
