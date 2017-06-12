from django.conf.urls import url
from django.contrib import admin
from loginsys import views as login_views


urlpatterns = [
    url(r'^login/$', login_views.login, name='login'),
    url(r'^logout/$', login_views.logout, name='logout'),
    url(r'^register/$', login_views.register, name='register'),

]