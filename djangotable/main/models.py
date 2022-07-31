from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField('Наименование оборудования', max_length=100)
    adoption = models.CharField('Дата принятия к учету', max_length=75, blank=True)
    number = models.CharField('Инвентарный номер', default=False, max_length=100)
    initial_cost = models.FloatField('Первоначальная стоимость', null=True, blank=True)
    calculate_depreciation = models.FloatField ('Стоимость для вычисления амортизации', null=True, blank=True)
    cost_begining_period = models.FloatField('Стоимость на начало периода', null=True, blank=True)
    depreciation_begining_period = models.FloatField('Амортизация на начало периода', null=True,blank=True)
    residual_value_begining = models.FloatField('Остаточная стоимость на начало периода', null=True,blank=True)
    price_end_period = models.FloatField('Стоимость на конец периода', null=True, blank=True)
    depreciation_end_period = models.FloatField('Амортизация на конец периода', null=True,blank=True)
    residual_value = models.FloatField('Остаточная стоимость', null=True,blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Список оборудования'
        verbose_name_plural = 'Списки оборудования'
