from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=250, null=True)
    product_code = models.CharField(max_length=250, null=True)
    price = models.FloatField(default=0)
    gst = models.IntegerField(default=0)
    food_product = models.BooleanField(default=False)