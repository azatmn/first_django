from django.urls import path, include
from stations.views import index, bus_stations

urlpatterns = [
    path('', include('stations.urls')),
    path('bus_stations/', bus_stations, name='bus_stations'),
]
