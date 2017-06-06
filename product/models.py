from __future__ import unicode_literals
from django.db import models
#from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.


class Category(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Каталог товаров'
    category_title = models.CharField(max_length=20, verbose_name="Категория")
    category_parent = models.ForeignKey('self', blank=True, null=True, default=None)


class Product(models.Model):
    class News(models.Model):
        class Meta:
            verbose_name = 'Товар'
            verbose_name_plural = 'Товары'
    product_name = models.CharField(max_length=30, verbose_name="Нзавания товара")
    product_overview = models.TextField(verbose_name="Обзор", blank=True)
    product_image = models.ImageField(upload_to='images/product/', verbose_name='Картинка товара')
    product_prices = models.IntegerField(verbose_name="Цена")
    product_date_create = models.DateTimeField(auto_now_add=True)
    product_date_update = models.DateTimeField(auto_now=True)
    product_categry = models.ForeignKey(Category, blank=True, null=True, default=None)

    def __unicode__(self):
        return self.product_name


    def get_overview_anons(self):
        return self.product_overview[:30]






