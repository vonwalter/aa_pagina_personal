from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    # path('about/', views.about, name="about"),
    # path('resume/', views.resume, name="resume"),
    # path('portfolio/', views.portfolio, name="portfolio"),
    # path('portfolio/details/<int:id>', views.details, name='details'),
    # path('services/', views.services, name="services"),
    # path('contact/', views.contact, name="contact"),

]
