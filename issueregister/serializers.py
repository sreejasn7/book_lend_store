from rest_framework import serializers
from .models import RentBooks

class RentBooksRelatedSerializer(serializers.ModelSerializer):
    book_name = serializers.ReadOnlyField(source='book.name', read_only=True)
    book_id = serializers.ReadOnlyField(source='book.id', read_only=True)

    class Meta:
        model = RentBooks
        fields = ('book_name', 'book_id',)
