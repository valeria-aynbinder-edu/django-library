from django.urls import path

from . import views

# Creating URLConf
urlpatterns = [
    # the order is important!!!
    path("books/<str:book_name>", views.book_by_name, name="book_by_name"),
    path('books', views.books, name='books'),
    path('customers/add', views.add_customer, name='add_customer'),
    path('customers/<int:customer_id>', views.customer_details, name='customer_details'),
    path('customers', views.customers, name='customers'),

    path('', views.index, name='index'),
]