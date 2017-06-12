from django.shortcuts import render, get_object_or_404, redirect
from django.template.context_processors import csrf

from comments.models import Comment
from loginsys.forms import UserCreateProfile
from product.models import Product, Category
from django.contrib import auth


def index(request):
    category_parent = Category.objects.filter(category_parent=None)
    category_chaild = [i for i in Category.objects.all() if i.category_parent in category_parent]
    category_chaild_not = [i for i in category_parent for j in category_chaild if i == j.category_parent]
    data = {
        'products': Product.objects.filter(is_public=True),
        'categorys': category_parent,
        'category_chaild': category_chaild,
        'category_chaild_not': category_chaild_not,
        'username': auth.get_user(request).username,
        'form': UserCreateProfile(),
    }

    data.update(csrf(request))

    if request.POST:
        newuser_form = UserCreateProfile(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(username=newuser_form.cleaned_data['username'],
                                        password=newuser_form.cleaned_data['password2'])
            auth.login(request, newuser)
            return redirect('/')
        else:
            data['form'] = newuser_form

    return render(request, 'product/index.html', data)


def get_product(request, id):
    category_parent = Category.objects.filter(category_parent=None)
    category_chaild = [i for i in Category.objects.all() if i.category_parent in category_parent]
    category_chaild_not = [i for i in category_parent for j in category_chaild if i == j.category_parent]

    data = {
        'product': get_object_or_404(Product, id=id),
        'categorys': category_parent,
        'category_chaild': category_chaild,
        'comments': Comment.objects.filter(comment_product_id=id),
        'category_chaild_not': category_chaild_not,
        'username': auth.get_user(request).username,

    }
    return render(request, 'product/product.html', data)


def get_category(request, slug):
    category = Category.objects.get(category_slug=slug)
    category_parent = Category.objects.filter(category_parent=None)
    category_chaild = [i for i in Category.objects.all() if i.category_parent in category_parent]
    category_chaild_not = [i for i in category_parent for j in category_chaild if i == j.category_parent]
    category_chailds = [i for i in category_chaild if category == i.category_parent]
    products = list()
    for i in category_chailds:
        products += i.get_product()
    products += category.get_product()
    data = {
        'products': products,
        'category': category,
        'categorys': category_parent,
        'category_chaild': category_chaild,
        'category_chaild_not': category_chaild_not,
        'username': auth.get_user(request).username,
    }
    return render(request, 'product/category.html', data)



