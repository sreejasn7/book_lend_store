from django.shortcuts import render
from django.contrib.auth.models import User
from bookkeeping.models import Book
from .models import RentBooks
from django.http import JsonResponse

from rest_framework import generics
from .serializers import RentBooksRelatedSerializer
from rest_framework.response import Response

def view_rent_page(request):
    user = User.objects.filter(is_superuser=False)
    return render(request, 'wishlist.html', {'customers': user})


class RentBooksList(generics.ListAPIView):
    queryset = {}
    serializer_class = RentBooksRelatedSerializer

    # def list(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(RentBooks.objects.filter(customer=request.user.id))
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        queryset = self.filter_queryset(RentBooks.objects.filter(customer=request.POST["customer"]))
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)