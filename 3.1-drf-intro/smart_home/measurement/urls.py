from django.urls import path
from .views import SensorListCreateAPIView, SensorRetrieveUpdateAPIView, MeasurementCreateAPIView

urlpatterns = [
    path('sensors/', SensorListCreateAPIView.as_view(), name='sensors'),
    path('sensors/<int:pk>/', SensorRetrieveUpdateAPIView.as_view(), name='sensor-detail'),
    path('measurements/', MeasurementCreateAPIView.as_view(), name='measurements'),
]
