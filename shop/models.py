from django.db import models

# Create your models here.


class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default="02")
    image = models.ImageField(upload_to="shop/images", default="")
    product_desc = models.CharField(max_length=200)
    pub_date = models.DateField()

    def __str__(self):
        return self.product_name


class Reg(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    mobile = models.IntegerField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name

