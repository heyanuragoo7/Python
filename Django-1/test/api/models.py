from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=128)
    age = models.IntegerField()
    role = models.CharField(max_length=20, default='user')  # Added role field as used in views

class Blog(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    owner = models.ForeignKey(Users, related_name='blog', on_delete=models.CASCADE)

class Cart(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=1)
    