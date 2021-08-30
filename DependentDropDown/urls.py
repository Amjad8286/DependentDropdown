from django.contrib import admin
from django.urls import path
from dropdown.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('load-state/', load_state, name='ajax_load_state'),
    path('load-city/', load_city, name='ajax_load_city'),
    path('lazy-state/', dropdownLazyState.as_view(), name='ajax_state'),
    path('lazy-city/<int:cid>', dropdownLazyCity.as_view(), name='lazy-city'),
]
