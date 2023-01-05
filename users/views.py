from django.shortcuts import render
from .models import House, Apartment, Shop
from django.views.generic import DetailView, ListView


# Create your views here.
def show_all_places(request):
    return render(request, 'home.html')

# def show_available_house(request):
#     houses = House.objects.all()
#     return render(request, 'house_list.html', {'houses': houses})


# class PlaceList(ListView):
#     model = House
#     app = "users"
#     template_name = f"{app}/{model.__name__.lower()}.html"
#     # queryset = model.objects.all()


class HouseList(ListView):
    model = House
    template_name = 'users/house.html'


# def show_available_apartment(request):
#     apartments = Apartment.objects.all()
#     return render(request, 'apartment_list.html', {'apartments': apartments})


class ApartmentList(ListView):
    model = Apartment
    template_name = 'users/apartment.html'


# def show_available_shop(request):
#     shops = Shop.objects.all()
#     return render(request, 'shop_list.html', {'shops': shops})


class ShopList(ListView):
    model = Shop
    template_name = 'users/shop.html'


# class HouseDetail(DetailView):
#     # model = House
#     model = Shop
#     app = "users"
#     template_name = f"{app}/{model.__name__.lower()}_detail.html"

class HouseDetail(DetailView):
    model = House


class ApartmentDetail(DetailView):
    model = Apartment


class ShopDetail(DetailView):
    model = Shop