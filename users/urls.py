from django.contrib import admin
from django.urls import path, include
from .views import show_all_places, show_available_apartment, show_available_house, show_available_shop

urlpatterns = [
    path('', show_all_places),
    path('house/', show_available_house, name='house'),
    path('apartment/', show_available_apartment, name='apartment'),
    path('shop/', show_available_shop, name='shop'),
]
