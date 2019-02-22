from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length = 50)

class Account(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)

class Trade(models.Model):
    account = models.ForeignKey(Account, on_delete = models.CASCADE)
    timestamp = models.PositiveIntegerField()
    num_shares = models.PositiveIntegerField()
    book_value = models.DecimalField(decimal_places=3, max_digits=8)
    ticker = models.CharField(max_length = 10)

class Asset(models.Model):
    account = models.ForeignKey(Account, on_delete = models.CASCADE)


