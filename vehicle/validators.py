import re
from rest_framework.serializers import ValidationError


class TitleValidator:

    # def __int__(self, title):
    """В инит передаем поле, которое необходимо валидировать и сохраняем его"""
    #     self.field = 'title'   не получилось, поле задано непосредственно в call

    def __call__(self, value, field='title'):
        """В метод передается order_dict value,
        в переменной tmp_val приводим value к классу dict и получаем из него значение
         поля, которое необходимо валидировать"""
        reg = re.compile('^[a-zA-Z0-9\.\-\ ]+$')
        tmp_val = dict(value).get(field)
        if not bool(reg.match(tmp_val)):
            raise ValidationError('title is not correct')
