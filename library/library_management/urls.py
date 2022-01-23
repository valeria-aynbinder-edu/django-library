from django.urls import path

from . import views

# Creating URLConf
urlpatterns = [
    # the order is important!!!
    path("books/<str:book_name>", views.book_by_name, name="book_by_name"),
    path('books', views.books, name='books'),
    path('customers', views.customers, name='customers'),
    path('', views.index, name='index'),
]