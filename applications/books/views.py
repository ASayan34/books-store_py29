from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from applications.books.models import Book
from applications.books.serializers import BookSerializer
from applications.books.permissions import IsAdminOrIsOwner


class BooksListAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    

class CreateBookAPIView(generics.CreateAPIView):
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
       

class RetrieveBookAPIView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class UpdateBookAPIView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer    
    permission_classes = [IsAdminOrIsOwner]


class DeleteBookAPIView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrIsOwner]
