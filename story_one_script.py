import os,django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library.settings')
django.setup()
from django.contrib.auth.models import User
from bookkeeping.models import BookChargeSheet, Book

books_in_store = 20
try:
    u = User(username='admin')
    u.set_password('admin@123')
    u.is_superuser = True
    u.is_staff = True
    u.save()

except:
    print("User already Exists")


try:
    book_charges, created = BookChargeSheet.objects.get_or_create(story_type='S1', book_type='All', days=1, per_day_charge=1, min_charge=0, min_charge_days=0 )
except:
    print("Exception")

# INSERT BOOKS
try:
    book_charge_set=BookChargeSheet.objects.all()
    for charge in book_charge_set.iterator():
        for i in range(0, books_in_store):
            name = 'Book Number ' + str(i) +' Section ' + charge.story_type
            books, created = Book.objects.get_or_create(name=name, book_charge=charge)


except:
    print("Exception")









