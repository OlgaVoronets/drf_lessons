from django.urls import path

from vehicle.apps import VehicleConfig
from rest_framework.routers import DefaultRouter

from vehicle.views import CarViewSet, MotoCreateView, MotoListView, MotoRetrieveView, MotoUpdateView, MotoDestroyView, \
    MilageCreateView

app_name = VehicleConfig.name
router = DefaultRouter()
router.register(r'cars', CarViewSet, basename='cars')

urlpatterns = [
                  path('moto/create/', MotoCreateView.as_view(), name='moto_create'),
                  path('moto/', MotoListView.as_view(), name='moto_list'),
                  path('moto/<int:pk>/', MotoRetrieveView.as_view(), name='moto_view'),
                  path('moto/update/<int:pk>/', MotoUpdateView.as_view(), name='moto_update'),
                  path('moto/delete/<int:pk>/', MotoDestroyView.as_view(), name='moto_delete'),
                  # milage
                  path('milage/create/', MilageCreateView.as_view(), name='milage_create'),

              ] + router.urls
