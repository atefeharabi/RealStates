from django.shortcuts import render
from .models import House, Apartment, Shop
from django.views.generic import DetailView, ListView


# Create your views here.
def show_all_places(request):
    return render(request, 'home.html')

# def show_available_house(request):
#     houses = House.objects.all()
#     return render(request, 'house_list.html', {'houses': houses})


class HouseList(ListView):
    model = House

def show_available_apartment(request):
    apartments = Apartment.objects.all()
    return render(request, 'apartment_list.html', {'apartments': apartments})


class ApartmentList(ListView):
    model = Apartment

def show_available_shop(request):
    shops = Shop.objects.all()
    return render(request, 'shop_list.html', {'shops': shops})


class ShopList(ListView):
    model = Shop
