import unittest, time, re
from django.test import TestCase
from .views import calculate_price
from .models import Book, BookChargeSheet


class LogicTest(TestCase):

    def test_book_rent_story1(self):
        books_in_store = 5
        book_charges, created = BookChargeSheet.objects.get_or_create(story_type='S1', book_type='All', days=1,
                                                                      per_day_charge=1, min_charge=0, min_charge_days=0)

        book_charge_set = BookChargeSheet.objects.all()
        for charge in book_charge_set.iterator():
            for i in range(0, books_in_store):
                name = 'Book Test Number ' + str(i) + ' Section ' + charge.story_type
                books, created = Book.objects.get_or_create(name=name, book_charge=charge)

        num = 11
        book_obj = Book.objects.all().first()
        self.assertEqual(num, calculate_price(book_obj.id, num))


if __name__ == "__main__":
    unittest.main()