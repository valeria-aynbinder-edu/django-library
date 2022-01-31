from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.template import loader

from .forms import NewCustomerForm
from .models import Customer

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

# def index(request):
#     response_data = f'''
#     <h2>WELCOME TO THE LIBRARY!!!</h2>
#     <a href='books'>Go to Books page</a>
#     <br>
#     <a href='customers'>Go to Customers page</a>
#     '''
#     return HttpResponse(response_data)


# def books(request):
#     response_data = f'''
#     <h2>BOOKS PAGE</h2>
#     <br>
#     <h4>Books list:</h4>
#     <a href='books/american_tragedy'>American Tragedy by Charles Dickens</a>
#     '''
#     return HttpResponse(response_data)

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

#
# def customers(request):
#     filter_txt = request.GET['search_str']
#     # look for relevant customers
#     relevant_customers = {}
#     render(request, "template", context=relevant_customers)
#     return HttpResponse("Customers page")

# def add_customer(request):
#     if request.method == 'GET':
#         return render(request, template_name='library_management/new_customer.html')
#     elif request.method == 'POST':
#         first_name = request.POST['fname']
#         last_name = request.POST['lname']
#         bday = request.POST['bday']
#         new_customer = Customer(first_name=first_name, last_name=last_name, birth_date=bday)
#         new_customer.save()
#         customers_query_set = Customer.objects.all()
#         customers_list = [customer for customer in customers_query_set]
#         return render(request,
#                       template_name='library_management/customers.html',
#                       context={'customers': customers_list})

def customers(request):
    if request.method == 'GET':
        customers_query_set = Customer.objects.all()
        print(f"The query to be executed: {customers_query_set.query}")
        customers_list = [customer for customer in customers_query_set]
        return render(request,
                      template_name='library_management/customers.html',
                      context={'customers': customers_list})


def add_customer(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NewCustomerForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            first_name = form.cleaned_data['fname']
            last_name = form.cleaned_data['lname']
            bday = form.cleaned_data['bday']
            new_customer = Customer(first_name=first_name, last_name=last_name, birth_date=bday)
            new_customer.save()
            # redirect to a new URL:
            customers_query_set = Customer.objects.all()
            customers_list = [customer for customer in customers_query_set]
            return render(request,
                          template_name='library_management/customers.html',
                          context={'customers': customers_list},
                          status=302)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NewCustomerForm()

    return render(request, 'library_management/new_customer_form.html', {'form': form})

def customer_details(request, customer_id):
    customer = Customer.objects.get(pk=customer_id)
    print(type(customer))
    # print(f"The query to be executed: {customer.query}")
    return render(request,
                  template_name='library_management/customer_details.html',
                  context={'customer': customer})




#/customers?search_str=Moshe


def index(request):
    #option 1
    template = loader.get_template('library_management/index_inh.html')
    return HttpResponse(template.render(request=request))

    #option 2
    # return render(request, 'library_management/index.html')
    #don't forget to bind the template


# def books(request):
#     return render(request, 'library_management/books1.html',
#                   context={'book1_key': 'american_tragedy',
#                            'book2_key': 'alice',
#                            'book1_name': books_data['american_tragedy']['name'],
#                            'book2_name': books_data['alice']['name']})


def books(request):
    return render(request, 'library_management/books_inh.html',
                  context={'books': books_data.items()})
