from rest_framework import serializers

from vehicle.models import Car, Moto, Milage


class CarSerializer(serializers.ModelSerializer):
    """Работа со встроенными полями
    Модель milage ссылается по foreignKey на модель Car,
    поэтому Car имеет свой milage_set(набор пробегов для конкретной машины).
    Ниже способ достать последний(самый новый если сортировка в обратном порядке, иначе - last). """
    last_milage = serializers.IntegerField(source='milage_set.all.first.milage')

    class Meta:
        model = Car
        fields = '__all__'


class MotoSerializer(serializers.ModelSerializer):
    """"""
    last_milage = serializers.SerializerMethodField()

    class Meta:
        model = Moto
        fields = '__all__'

    def get_last_milage(self, obj):
        if obj.milage_set.all().first():
            return obj.milage_set.all().first().milage
        return 0


class MilageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Milage
        fields = '__all__'
