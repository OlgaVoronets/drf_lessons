from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics

from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated

from vehicle.models import Car, Moto, Milage
from vehicle.paginators import VehiclePaginator
from vehicle.permissions import IsOwnerOrStaff
from vehicle.serializers import CarSerializer, MotoSerializer, MilageSerializer, MotoMilageSerializer, \
    MotoCreateSerializer


class CarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
    permission_classes = [IsAuthenticated]  # если в сеттингах 'DEFAULT_PERMISSION_CLASSES': AllowAny'

    # def post(self, *args, **kwargs):
    #     """кастомизация сериализатора для вьюсета"""
    #     self.serializer_class = """новый класс сериализатор"""


class MotoCreateView(generics.CreateAPIView):
    serializer_class = MotoCreateSerializer
    permission_classes = [IsAuthenticated]

    #  Присваивем владельца при создании объекта

    def perform_create(self, serializer):
        new_moto = serializer.save()  # работа метода в родительском классе
        new_moto.owner = self.request.user
        new_moto.save()


class MotoListView(generics.ListAPIView):
    serializer_class = MotoSerializer
    queryset = Moto.objects.all()
    pagination_class = VehiclePaginator


class MotoRetrieveView(generics.RetrieveAPIView):
    serializer_class = MotoSerializer
    queryset = Moto.objects.all()


class MotoUpdateView(generics.UpdateAPIView):
    serializer_class = MotoSerializer
    queryset = Moto.objects.all()
    permission_classes = [IsOwnerOrStaff]


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
    queryset = Milage.objects.filter(moto__isnull=False)  # Пробеги фильтруем по полю мото (не пустое)
    serializer_class = MotoMilageSerializer
