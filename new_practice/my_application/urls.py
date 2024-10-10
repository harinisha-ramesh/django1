from django.urls import path
from .views import *

urlpatterns = [
    path('home/',homepage),
    path('about/',about),
    path('contact/',contact.as_view(),name = 'contact'),
    path('services/',service.as_view(),name='services'),
    path('products/add/',ProductsAdd.as_view(), name= 'add-products'),
    path('products/',AllProducts.as_view(),name = 'all-products'),
]

