from django.urls import path
from .views import *

urlpatterns = [
    path('home/',homepage),
    path('about/',about),
    path('contact/',contact.as_view()),
    path('services/',service.as_view()),
]

