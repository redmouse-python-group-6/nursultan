from django.conf.urls import url
from django.contrib import admin
from product import views as product_views


urlpatterns = [
    url(r'^(?P<id>\w+)/$', product_views.get_product, name='get_product'),
    #url(r'^cat/(?P<id>\w+)/^$', product_views.get_category, name='get_category')
]