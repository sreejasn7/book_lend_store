import os,django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'timetable.settings')
django.setup()
from django.contrib.auth.models import User
from bookkeeping.models import BookChargeSheet

try:
    u = User(username='admin')
    u.set_password('admin@123')
    u.is_superuser = True
    u.is_staff = True
    u.save()

except:
    print("User already Exists")


try:
    book = BookChargeSheet(book_type='all', days=1, per_day_charge=1, min_charge=0, min_charge_day=0 )
    book.save()

except:
    print("Exception")


# try:
#      BookChargeSheet.objects.all()
#     book.save()
#
# except:
#     print("Exception")










