from django.conf.urls import url
from django.contrib import admin
from product import views as product_views


urlpatterns = [
    url(r'^(?P<id>\w+)/$', product_views.get_artcile, name='get_product'),
]