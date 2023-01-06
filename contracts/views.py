from django.shortcuts import render, HttpResponse
from django.views import View
from users.models import *
from .models import Contract

# Create your views here.


class ContractApartment(View):
    model = Apartment

    def get(self, request, obj_id):
        apt = self.model.objects.get(id=obj_id)
        return render(request, 'contracts/contract.html', {'apt': apt})

    def post(self, request, obj_id):
        date = request.POST.get('date')
        ex_date = request.POST.get('ex_date')
        apt_obj = self.model.objects.get(id=obj_id)
        owner = apt_obj.owner
        customer = User.objects.get(id=1)
        new_contract = Contract(owner=owner, customer=customer, contract_date=date, expire=ex_date,
                                A_fk=apt_obj)
        new_contract.save()
        return HttpResponse('contract successfully created...')


class ContractHouse(View):
    pass
    # def get(self, request, obj_id):
    #     return render(request, 'contracts/contract.html')



class ContractShop(View):
    pass





