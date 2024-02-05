from rest_framework import viewsets, generics

from vehicle.models import Car, Moto
from vehicle.serializers import CarSerializer, MotoSerializer


class CarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()


class MotoCreateView(generics.CreateAPIView):
    serializer_class = MotoSerializer


class MotoListView(generics.ListAPIView):
    serializer_class = MotoSerializer
    queryset = Moto.objects.all()


class MotoRetrieveView(generics.RetrieveAPIView):
    serializer_class = MotoSerializer
    queryset = Moto.objects.all()


class MotoUpdateView(generics.UpdateAPIView):
    serializer_class = MotoSerializer
    queryset = Moto.objects.all()


class MotoDestroyView(generics.DestroyAPIView):
    queryset = Moto.objects.all()