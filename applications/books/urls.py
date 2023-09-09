from django.urls import path
from applications.books.views import BooksListAPIView, CreateBookAPIView, RetrieveBookAPIView, UpdateBookAPIView, DeleteBookAPIView


urlpatterns = [
    path('', BooksListAPIView.as_view()),
    path('create/', CreateBookAPIView.as_view()),
    path('<int:pk>/', RetrieveBookAPIView.as_view()),
    path('update/<int:pk>/', UpdateBookAPIView.as_view()),
    path('delete/<int:pk>/', DeleteBookAPIView.as_view())
]