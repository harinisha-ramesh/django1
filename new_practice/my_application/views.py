from django.shortcuts import render
from django.views import View
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .forms import *
from .models import *

def homepage(request):
    data = {
        "name" : "Nick",
        "age" : 25,
        "role": "Admin",
        "numbers": [1,2,3,4,5],
        "marks":{
            "Tamil":97,
            "English":92
        }
    }
    return render(request, 'home.html',data)

def about(request):
    info = {
        "company_name": "E2 Infosystems",
        "description": "A customer driven technology company",
        "team": ["John","Ram","Raju","Nick"]
    }
    return render(request,'about.html',info)

class service(View):
    def get(self,request):
        service_data = {
            "services": [{"name": "Web Development", "description": "Building modern websites"},
                {"name": "App Development", "description": "Creating mobile applications"},
                {"name": "SEO Services", "description": "Optimizing your site for search engines"}]
        }
        return render (request,'services.html',service_data)
    
class contact(View):
    def get(self,request):
        contact_info = {
            "email": "support@e2infosystems.com",
            "phone": 9087654321,
            "Address": "123 Tech Park, Silicon Valley"
        }    
        return render (request,'contact.html',contact_info)
    
class AllProducts(ListView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'all_products'

class ProductsAdd(CreateView):
    model = Product
    form_class = Product_Form
    template_name = 'products_add.html'
    success_url = reverse_lazy('all-products')

class ProductsUpdate(UpdateView):
    model = Product
    form_class = Product_Form
    template_name = 'products_update.html'
    success_url = reverse_lazy('all-products')

class ProductsDelete(DeleteView):
    model = Product
    template_name = 'products_delete.html'
    success_url = reverse_lazy('all-products')

# def ProductsAdd(request):

#     add = {
#         'product_add' : Product_Form
#     }
#     if request.method == "POST":
#         product_add = Product_Form(request.POST)

#         if product_add.is_valid():
#             product_add.save()

#     return render(request,'products_add.html', add)  

# def AllProducts(request):
#     context = {
#         'all_products' : Product.objects.all()
#     } 
#     return render(request,'products.html',context)    