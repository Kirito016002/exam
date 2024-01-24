from django.urls import path
from . import views

urlpatterns = [
    # Asosiy menu uchun 
    path("", views.index, name="index"),
    # Murojatlar oynasi uchun 
    path("contact", views.contact, name="contact"),
    # Xizmatlar oynasi uchun 
    path("services", views.services, name="services"),
    # Blog oynasi uchun 
    path("blog", views.blog, name="blog"),
]