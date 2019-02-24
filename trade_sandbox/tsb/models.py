from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return "User: {self.name}"

class Account(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return "Account: {self.id}" 

class Trade(models.Model):
    account = models.ForeignKey(Account, on_delete = models.CASCADE)
    timestamp = models.PositiveIntegerField()
    num_shares = models.PositiveIntegerField()
    book_value = models.DecimalField(decimal_places=3, max_digits=8)
    ticker = models.CharField(max_length = 10)

    def __str__(self):
        return "Trade: {self.id} - {self.ticker} - {self.timestamp}"

class Asset(models.Model):
    account = models.ForeignKey(Account, on_delete = models.CASCADE)
    trade = models.ForeignKey(Trade, on_delete = models.CASCADE)

    def __str__(self):
        return "Asset: {self.id}"


