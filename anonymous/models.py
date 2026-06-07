from django.db import models

# Create your models here.


class Register(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Food(models.Model):

    CATEGORY_CHOICES = (
        ('Pizza', 'Pizza'),
        ('Burger', 'Burger'),
        ('Momos', 'Momos'),
        ('Drinks', 'Drinks'),
    )

    name = models.CharField(max_length=100)

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='Pizza'
    )

    description = models.TextField(default="")

    price = models.IntegerField()

    image = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Cart(models.Model):

    user = models.ForeignKey(Register,on_delete=models.CASCADE)
    food = models.ForeignKey(Food,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    def __str__(self):
        return self.user.name


class Order(models.Model):

    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Preparing', 'Preparing'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    )

    user = models.ForeignKey(Register, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total_price = models.IntegerField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    def __str__(self):
        return self.user.name