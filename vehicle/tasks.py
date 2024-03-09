from celery import shared_task
from django.core.mail import send_mail

from vehicle.models import Car, Moto


@shared_task
def check_milage(pk, model):
    if model == 'Car':
        instance = Car.objects.filter(pk=pk).first()
    else:
        instance = Moto.objects.filter(pk=pk).first()
    if instance:
        prev_milage = -1
        for m in instance.milage.all():
            if prev_milage == -1:
                prev_milage = m.milage
            else:
                """Если сортировка от большего к меньшему, 
                то пред.пробег должен быть больше текущего"""
                if prev_milage < m.milage:
                    """Тут можно отправить письмо модератору или владельцу, заблокировать машину и тд"""
                    print('Неверный пробег')
                    break


def check_filter():
    filter_price = {'amount__lte': 2000}
    if Car.objects.filter(**filter_price).exists():
        print('Отчет по фильтру')
        # send_mail(
        #     subject='Отчет по фильтру',
        #     message='По вашему запросу есть результаты',
        #     from_email='no_answer@mail.com',
        #     recipient_list=[user.email]
        # )

