from django.conf import settings
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Car(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE)
    amount = models.IntegerField(default=1000, verbose_name='Цена')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'


class Moto(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE)
    amount = models.IntegerField(default=1000, verbose_name='Цена')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Мотоцикл'
        verbose_name_plural = 'Мотоциклы'


class Milage(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='milage', **NULLABLE)
    moto = models.ForeignKey(Moto, on_delete=models.CASCADE, related_name='milage', **NULLABLE)

    milage = models.PositiveIntegerField(verbose_name='Пробег')
    year = models.PositiveSmallIntegerField(verbose_name='Год регистрации')

    def __str__(self):
        return f'{self.moto if self.moto else self.car} - {self.year}'

    class Meta:
        verbose_name = 'Пробег'
        verbose_name_plural = 'Пробег'
        ordering = ('-year',)
