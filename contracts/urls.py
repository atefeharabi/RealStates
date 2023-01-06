from django.urls import path, include
from .views import *


urlpatterns = [
    path('apartment/<int:obj_id>', ContractApartment.as_view(), name='apartment-contract'),
    # path('apartment/<int:obj_id>', contract_apartment, name='apartment-contract'),
    path('house/', ContractHouse.as_view(), name='house_contract'),
    path('shop/', ContractShop.as_view(), name='shop_contract')
]

