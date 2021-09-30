from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

STATE_CHOICE = (
    ('PUNJAB', 'PUNJAB'),
    ('SINDH', 'SINDH'),
    ('KPK', 'KPK'),
    ('BALOCHISTAN', 'BALOCHISTAN'),
    ('GB', 'BG'),
)

CATAGORY_CHOICE = (
    ('M', 'MOBILE'),
    ('L', 'LAPTOP'),
    ('TW', 'TOP WEAR'),
    ('BW', 'BOTTOM WEAR'),
)
STATUS_CHOICE = (
    ('pending', 'pending'),
    ('accepted', 'accepted'),
    ('delivered', 'delivered'),
    ('canceled', 'canceled'),
)


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip_code = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICE, max_length=100)

    def __str__(self):
        return str(self.id)


class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discount_price = models.FloatField()
    city = models.CharField(max_length=100)
    description = models.TextField()
    brand = models.CharField(max_length=200)
    catagory = models.CharField(choices=CATAGORY_CHOICE, max_length=100)
    image = models.ImageField(upload_to='productimg')

    def __str__(self):
        return str(self.id)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)
    @property
    def total_cost(self):
        return self.quantity * self.product.discount_price


class Order_Placed(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS_CHOICE, max_length=50, default='pending')

    def __str__(self):
        return str(self.id)
