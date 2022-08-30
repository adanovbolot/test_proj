from django.db import models
from car.choice import CHOICE_PHONE, DEFAULT


class BaseAbstractCategory(models.Model):
    class Meta:
        abstract = True

    email = models.EmailField(verbose_name='Эл.почта')
    user_type = models.CharField(max_length=100, verbose_name='ИП или Юр.лицо')
    inn = models.CharField(max_length=15, verbose_name='ИИН')
    city = models.CharField(max_length=50, verbose_name='Ваш город')
    the_outside = models.CharField(max_length=100, verbose_name='Улица')
    home_residential = models.CharField(max_length=100, verbose_name='Дом/стр.')
    office = models.CharField(verbose_name='Офис', max_length=100)
    phone_code = models.CharField(max_length=100, verbose_name='Код', choices=CHOICE_PHONE, default=DEFAULT)
    phone_number = models.IntegerField(blank=True, verbose_name='Номер телефона')
    score = models.BooleanField('Магазин', default=False, blank=True)
    regional_chain_store = models.BooleanField('Региональная сеть магазина', default=False, blank=True)
    federal_store_chain = models.BooleanField('Федеральная сеть магазина', default=False, blank=True)
    online_store = models.BooleanField('Интернет-магазин', default=False, blank=True)
    car_service = models.BooleanField('Автосервис', default=False, blank=True)
    other = models.CharField(max_length=200, blank=True, null=True, verbose_name='Прочее')
    boo = models.BooleanField('', default=False)


class RegisterBuyer(BaseAbstractCategory):
    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'

    def __str__(self):
        return f"{BaseAbstractCategory.email}"


class RegisterProvider(BaseAbstractCategory):
    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'

    site = models.URLField(verbose_name='Сайт Вашей компании', max_length=100, blank=True)

    def __str__(self):
        f'{BaseAbstractCategory.email}'

