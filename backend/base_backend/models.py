from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    _id = models.AutoField(primary_key=True,editable=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(null=True, blank=True) #  will add default and upload_to later
    name = models.CharField(max_length=200, null=True, blank=True)
    category = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    brand = models.CharField(max_length=200, null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    rating = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    review_count = models.IntegerField(null=True, blank=True, default=0)
    in_stock_count = models.IntegerField(null=True, blank=True, default=0)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + "-" + self.brand + "-" + self.category + "-" + str(self.price)


class Order(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    total_price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    tax_price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    shipping_price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    is_payment_successful = models.BooleanField(default=False)
    is_delivered = models.BooleanField(default=False)
    payment_time = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    delivery_time = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return str(self.create_time)


class OrderItems(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True, default=0)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Address(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    address1 = models.CharField(max_length=200, null=False, blank=False)
    address2 = models.CharField(max_length=200, null=True, blank=True)
    post_code = models.CharField(max_length=10, null=True, blank=True)
    city = models.CharField(max_length=85, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    order = models.OneToOneField(Order, on_delete=models.CASCADE, null=True, blank=True)
    shipping_price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return str(self.address1)
