from django.db import models


class BookChargeSheet(models.Model):
    story_type = models.CharField(max_length=10, blank=False)
    book_type = models.CharField(max_length=30)
    days = models.IntegerField()
    per_day_charge = models.FloatField()
    min_charge = models.FloatField()
    min_charge_days = models.IntegerField()

    def __str__(self):
        return self.book_type


class Book(models.Model):
    name = models.CharField(max_length=100)
    book_charge = models.ForeignKey(BookChargeSheet, on_delete=models.CASCADE)

    def __str__(self):
        return self.name