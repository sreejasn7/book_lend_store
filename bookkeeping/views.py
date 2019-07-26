from django.shortcuts import render, redirect
from bookkeeping.models import Book
from django.contrib import messages
from issueregister.models import RentBooks, Book
from django.contrib.auth.models import User
from .models import BookChargeSheet
from django.http import JsonResponse
from django.forms.models import model_to_dict


def book_keeping_index(request, book_type_id=0):
    if book_type_id == 0:
        books = Book.objects.all()
    else:
        books = Book.objects.filter(book_charge=book_type_id)
    return render(request, 'shop-grid.html', {"list_books":books})


def book_detail(request, book_id=0):
    book_preview = Book.objects.get(id=book_id)
    return render(request, 'single-product.html', {"book_details": book_preview})


def rent_books(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            book_obj = Book.objects.get(id=request.POST['book_id'])
            user_obj = User.objects.get(id=request.user.id)
            books, created = RentBooks.objects.get_or_create(book=book_obj, customer=user_obj)
            if created:
                messages.success(request, 'Rented.')
            else:
                messages.success(request, 'Already Rented before.')
            return redirect(request.META['HTTP_REFERER'])
    else:
        return redirect('/register')


def get_book_charge_sheet(request):
    dataset = BookChargeSheet.objects.all()
    result_book_dict = []
    for i in dataset:
        result_book_dict.append(model_to_dict(i))
    return_dict = {'book_types':result_book_dict}
    return JsonResponse(return_dict, safe=True)


def get_book_rent_price(request):
    result_array = request.POST['result'].split('&')
    total = 0
    for i in result_array:
        key_value = i.split('=')
        total += calculate_varying_price(int(key_value[0]), int(key_value[1]))
    return_dict = {'success': True, 'total': total}
    return JsonResponse(return_dict, safe=True)


def calculate_price(book_id, num):
    book_obj = Book.objects.get(id=book_id)
    rent = num * book_obj.book_charge.per_day_charge
    return rent


def calculate_varying_price(book_id,num):
    book_obj = Book.objects.get(id=book_id)
    rent = 0
    if book_obj.book_charge.min_charge != 0:
        if num <= book_obj.book_charge.min_charge_days:
            rent += book_obj.book_charge.min_charge
        else:
            rent += ((num - book_obj.book_charge.min_charge_days) * book_obj.book_charge.per_day_charge) +  book_obj.book_charge.min_charge
    else:
        rent = num * book_obj.book_charge.per_day_charge

    return rent



