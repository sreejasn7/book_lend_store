from django.contrib import admin

# Register your models here.

from django.contrib import admin
from bookkeeping.models import BookChargeSheet

class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(BookChargeSheet, AuthorAdmin)