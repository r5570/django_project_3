from django.shortcuts import render,redirect
from django.http import HttpResponse

from django.urls import reverse_lazy
from django.template import loader
from .models import Product #importing the Product from the models

from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView
# Create your views here.


def home(request):
    home=''
    context={

    }
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context,request))

def productlist(request):
    products=Product.objects.all() #querying all records in the DB  OF ENTITY TYPE ' Product'
    context = {

        'prods' : products #the key prods will now be Available to  use in the django template design

    } #context dictionary for passing data for rendering
    template = loader.get_template('product.html') #template object from the designed template html
    return HttpResponse(template.render(context,request)) #creates a response object after rendering
    # the returned response has the html of completed webpage including required data


# view functions for rendering individual product page
def product_details(request,id):  #This is equivalent 
    product = Product.objects.get(id = id) #select * from products where id =<parameter id>
    context ={

        'prod' : product
    }


    template= loader.get_template('prod_details.html')
    return HttpResponse(template.render(context,request))

# CRUD
# C - Create
class AddProduct(CreateView):
    model= Product
    fields=[ #Speicifying the fields to be generated in the form
      
      'name',
      'price',
      'desc',
      'stock',
      'pic'

    ]
    template_name='addProduct.html'
    success_url=reverse_lazy('homepage')


# 2. R - Read

class ProductView(ListView):
    model = Product
    template_name ='productView.html'
    ordering=['-id'] # to sort in descending order


# 3. U - Update

class EditProduct(UpdateView):
    model=Product
    template_name='editProduct.html'
    success_url=reverse_lazy('homepage')


# 4. D - Delte
class DelProduct(DeleteView):
    model=Product
    template_name='delProduct.html'
    success_url=reverse_lazy('homepage')