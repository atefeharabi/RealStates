from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', show_all_places),
    # path('house/', show_available_house, name='house'),
    path('house/', HouseList.as_view()),
    # path('house/', PlaceList.as_view()),
    # path('apartment/', show_available_apartment, name='apartment'),
    path('apartment/', ApartmentList.as_view()),
    # path('apartment/', PlaceList.as_view(model=Apartment)),
    # path('shop/', show_available_shop, name='shop'),
    path('shop/', ShopList.as_view()),
    # path('shop/', PlaceList.as_view(model=Shop)),
    # path('house/<int:pk>', HouseDetail.as_view(model=House), name='house-detail'),
    # path('apartment/<int:pk>', HouseDetail.as_view(model=Apartment), name='apartment-detail'),
    # path('shop/<int:pk>', HouseDetail.as_view(model=Shop), name='shop-detail'),
    path('house/<int:pk>', HouseDetail.as_view(), name='house-detail'),
    path('apartment/<int:pk>', ApartmentDetail.as_view(), name='apartment-detail'),
    path('shop/<int:pk>', ShopDetail.as_view(), name='shop-detail'),

]
