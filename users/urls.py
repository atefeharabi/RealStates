from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', show_all_places),
    # path('house/', show_available_house, name='house'),
    path('house/', HouseList.as_view()),
    # path('apartment/', show_available_apartment, name='apartment'),
    path('apartment/', ApartmentList.as_view()),
    # path('shop/', show_available_shop, name='shop'),
    path('shop/', ShopList.as_view()),

]
