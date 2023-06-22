from django.urls import path
from .views import cus_detail, cus_list, book_list, author_list

urlpatterns = [
    path('customer/<int:pk>/', cus_detail, name='detail'),
    path('customer', cus_list, name='list'),
    path('author', author_list, name="author"),
    path('book', book_list, name="book")
]
