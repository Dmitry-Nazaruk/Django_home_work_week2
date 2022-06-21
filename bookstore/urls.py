from django.urls import path

from bookstore.views import list_books, book_description, infobook, infoauthor

urlpatterns = [
    path('', list_books, name='base'),
    path('<title>', book_description, name='book'),
    path('<title>/infobook', infobook),
    path('infoauthor/<int:index>', infoauthor)
]