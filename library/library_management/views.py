from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseNotFound

#
# def index(request):
#     return HttpResponse("Hi All! Welcome to our Library Web App")

# def books(request):
#     return HttpResponse("Books page")

books_data = {
    'american_tragedy': {
        'id': 1,
        'author': 'Charles Dickens',
        'name': 'American Tragedy',
        'publication_year': 2019
    },
    'alice': {
        'id': 2,
        'author': 'Lewis Carroll',
        'name': 'Alice in a Wonderland',
        'publication_year': 2017
    }
}

def index(request):
    response_data = f'''
    <h2>WELCOME TO THE LIBRARY!!!</h2>
    <a href='books'>Go to Books page</a>
    <br>
    <a href='customers'>Go to Customers page</a>
    '''
    return HttpResponse(response_data)


def books(request):
    response_data = f'''
    <h2>BOOKS PAGE</h2>
    <br>
    <h4>Books list:</h4>
    <a href='books/american_tragedy'>American Tragedy by Charles Dickens</a>
    '''
    return HttpResponse(response_data)

def book_by_name(request, book_name):
    try:
        book_data = books_data[book_name]
    except:
        return HttpResponseNotFound(f"This book does not exist in the library")

    response_data = f'''
    <h2>BOOK DETAILS</h2>
    <br>
    <h4>Book name: {book_data['name']}</h4>
    <h4>Author: {book_data['author']}</h4>
    <h4>Publication year: {book_data['publication_year']}</h4>
    '''
    return HttpResponse(response_data)
    # return HttpResponse("Books page")


def customers(request):
    return HttpResponse("Customers page")



