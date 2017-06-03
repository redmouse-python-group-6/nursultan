from django.db import models

# Create your models here.


class Product(models.Model):
    class News(models.Model):
        class Meta:
            verbose_name = 'Товар'
            verbose_name_plural = 'Товары'

    product_name = models.CharField(max_length=30, verbose_name="Нзавания товара")
    product_overview = models.TextField(verbose_name="Обзор")
    product_image = models.ImageField(upload_to='images/product/', verbose_name='Картинка товара')
    product_prices = models.IntegerField(verbose_name="Цена")
    product_date_create = models.DateTimeField(auto_now_add=True)
    product_date_update = models.DateTimeField(auto_now=True)


    def get_overview_anons(self):
        return self.product_overview[:30]



