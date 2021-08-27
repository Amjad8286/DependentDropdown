from django.shortcuts import render
from .models import *

def index(request):
    country = Country.objects.all()
    d = {'country': country}
    return render(request,'index.html',d)

def load_state(request):
    state_id = request.GET.get('country')
    state = State.objects.filter(country=state_id).order_by('state')
    return render(request, 'states.html', {'state': state})

def load_city(request):
    city_id = request.GET.get('state')
    print(city_id)
    city = City.objects.filter(state=city_id).order_by('city')
    return render(request, 'city.html', {'city': city})




