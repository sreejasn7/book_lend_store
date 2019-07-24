from django.db import models

# Create your models here.
from django.db import models
from bookkeeping.models import Book
from django.contrib.auth.models import User

class RentBooks(models.Model):
    book = models.ForeignKey(Book , on_delete=models.CASCADE)
    customer = models.ForeignKey(User , on_delete=models.CASCADE)

    def __str__(self):
        return self.customer.email
