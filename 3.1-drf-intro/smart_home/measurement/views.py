from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from .models import Sensor, Measurement
from .serializers import SensorSerializer, SensorDetailSerializer, MeasurementSerializer


class SensorListCreateAPIView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class SensorRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return SensorDetailSerializer  # для получения детальной информации с measurements
        return SensorSerializer  # для обновления (PATCH/PUT) - без measurements

class MeasurementCreateAPIView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer