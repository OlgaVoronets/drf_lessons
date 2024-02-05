from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics

from rest_framework.filters import OrderingFilter

from vehicle.models import Car, Moto, Milage
from vehicle.serializers import CarSerializer, MotoSerializer, MilageSerializer, MotoMilageSerializer, \
    MotoCreateSerializer


class CarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()

    # def post(self, *args, **kwargs):
    #     """кастомизация сериализатора для вьюсета"""
    #     self.serializer_class = """новый класс сериализатор"""


class MotoCreateView(generics.CreateAPIView):
    serializer_class = MotoCreateSerializer


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


class MilageCreateView(generics.CreateAPIView):
    serializer_class = MilageSerializer


class MilageListView(generics.ListAPIView):
    serializer_class = MilageSerializer
    queryset = Milage.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('car', 'moto')
    ordering_fields = ('year',)


class MotoMilageListView(generics.ListAPIView):
    """Для вывода пробегов мотоциклов реализовать описание объекта мотоцикла,
    которому принадлежит пробег."""
    queryset = Milage.objects.filter(moto__isnull=False)   #  Пробеги фильтруем по полю мото (не пустое)
    serializer_class = MotoMilageSerializer
