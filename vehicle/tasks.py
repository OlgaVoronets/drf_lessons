from celery import shared_task

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
