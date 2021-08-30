from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from .models import *

def index(request):
    country = Country.objects.all()
    d = {'country': country}
    return render(request,'index.html',d)


def load_state(request):
    state_id = request.GET.get('country')
    state = State.objects.filter(country=state_id).order_by('state')
    return render(request,'states.html',{'state': state})


def load_city(request):
    city_id = request.GET.get('state')
    city = City.objects.filter(state=city_id).order_by('city')
    return render(request,'city.html',{'city': city})

class dropdownLazyState(View):
    def get(self, *args, **kwargs):
        state = list(State.objects.values())
        return JsonResponse({'data':state})

class dropdownLazyCity(View):
    def get(self, *args, **kwargs):
        upper = kwargs.get('cid')
        lower = upper - 5
        city = list(City.objects.values()[lower:upper])
        return JsonResponse({'data':city})
       