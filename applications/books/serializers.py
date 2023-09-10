from rest_framework import serializers
from applications.books.models import Book

class BookSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = Book
        fields = '__all__'
        