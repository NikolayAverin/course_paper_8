from django.db import models
from config import settings

NULLABLE = {'blank': True, 'null': True}
HABIT_TIME = [
    ('morning', 'утром'),
    ('day', 'днем'),
    ('evening', 'вечером'),
    ('anytime', 'в любое время'),
]
HABIT_PERIOD = [
    ('daily', 'ежедневно'),
    ('every two days', 'раз в два дня'),
    ('every three days', 'раз в три дня'),
    ('every four days', 'раз в четыре дня'),
    ('every five days', 'раз в пять дней'),
    ('every six days', 'раз в шесть дней'),
    ('weekly', 'раз в неделю'),
]


class Habit(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='Создатель привычки')
    place = models.CharField(max_length=200, verbose_name='Место выполнения привычки', help_text='Введите место, где необходимо выполнять привычку')
    time = models.CharField(max_length=20, choices=HABIT_TIME, verbose_name='Время выполнения привычки', help_text='Укажите время, в которое необходимо выполнять привычку')
    description = models.TextField(verbose_name='Описание привычки', help_text='Опишите, что необходимо сделать')
    is_pleasant_habit = models.BooleanField(verbose_name='Признак приятной привычки', help_text='Выберите, является ли эта привычка приятной')
    related_habit = models.ForeignKey('self', on_delete=models.SET_NULL, **NULLABLE, verbose_name='Связанная привычка', help_text='Выберите приятную привычку за выполнение полезной')
    period = models.CharField(max_length=20, choices=HABIT_PERIOD, default='daily', verbose_name='Период выполнения привычки', help_text='Укажите период, в котором необходимо выполнять привычку')
    award = models.TextField(verbose_name='Вознаграждение', help_text='Введите вознаграждение за выполнение полезной привычки')
    time_to_complete = models.PositiveIntegerField(verbose_name='Время на выполнение привычки', help_text='Введите время в секундах на выполнение привычки, до 120 сек')
    is_public = models.BooleanField(verbose_name='Признак публичной привычки', help_text='Выберите, является ли привычка публичной')

    def __str__(self):
        return f'{self.description}: {self.time} в {self.place}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
