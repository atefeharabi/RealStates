from django.shortcuts import render
from .models import House, Apartment, Shop


# Create your views here.
def show_all_places(request):
    return render(request, 'home.html')

def show_available_house(request):
    houses = House.objects.all()
    return render(request, 'house.html', {'houses': houses})


def show_available_apartment(request):
    apartments = Apartment.objects.all()
    return render(request, 'apartment.html', {'apartments': apartments})


def show_available_shop(request):
    shops = Shop.objects.all()
    return render(request, 'shop.html', {'shops': shops})