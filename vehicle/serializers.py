from rest_framework import serializers

from vehicle.models import Car, Moto, Milage
from vehicle.services import convert_currencies
from vehicle.validators import TitleValidator


class MilageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Milage
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    """Работа со встроенными полями
    Модель milage ссылается по foreignKey на модель Car,
    поэтому Car имеет свой milage_set(набор пробегов для конкретной машины).
    Ниже способ достать последний(самый новый если сортировка в обратном порядке, иначе - last). """
    last_milage = serializers.IntegerField(source='milage.all.first.milage', read_only=True)
    milage = MilageSerializer(many=True, read_only=True)
    usd_prise = serializers.SerializerMethodField()

    class Meta:
        model = Car
        fields = '__all__'
        validators = [TitleValidator(),
                      serializers.UniqueTogetherValidator(fields=['title', 'description'], queryset=Car.objects.all())
                      ]

    def get_usd_prise(self, instance):
        return convert_currencies(instance.amount)


class MotoSerializer(serializers.ModelSerializer):
    """"""
    last_milage = serializers.SerializerMethodField()

    class Meta:
        model = Moto
        fields = '__all__'

    def get_last_milage(self, obj):
        if obj.milage.all().first():
            return obj.milage.all().first().milage
        return 0


class MotoMilageSerializer(serializers.ModelSerializer):
    moto = MotoSerializer()

    class Meta:
        model = Milage
        fields = ('milage', 'year', 'moto')


class MotoCreateSerializer(serializers.ModelSerializer):
    milage = MilageSerializer(many=True)

    class Meta:
        model = Moto
        fields = '__all__'
        validators = [TitleValidator(),
                      serializers.UniqueTogetherValidator(fields=['title', 'description'], queryset=Moto.objects.all())
                      ]

    def create(self, validated_data):
        """убираем набор объектов по ключу 'milage', тк у мото нет поля миладж и добавить его туда нельзя"""
        milage = validated_data.pop('milage')

        moto_item = Moto.objects.create(**validated_data)
        for m in milage:
            """Цикл по каждому пробегу из сета миладж, для каждого создаем объект 
            класса миладж со ссылкой на мото, который, собссно, создаем"""
            Milage.objects.create(**m, moto=moto_item)
        return moto_item
