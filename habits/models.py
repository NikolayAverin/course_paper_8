from django.db import models

from config import settings

NULLABLE = {"blank": True, "null": True}
HABIT_TIME = [
    ("morning", "утром"),
    ("day", "днем"),
    ("evening", "вечером"),
    ("anytime", "в любое время"),
]


class Habit(models.Model):
    """Модель привычки"""

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        **NULLABLE,
        verbose_name="Создатель привычки",
    )
    place = models.CharField(
        max_length=200,
        verbose_name="Место выполнения привычки",
        help_text="Введите место, где необходимо выполнять привычку",
    )
    time = models.CharField(
        max_length=20,
        choices=HABIT_TIME,
        verbose_name="Время выполнения привычки",
        help_text="Укажите время, в которое необходимо выполнять привычку",
    )
    description = models.TextField(
        verbose_name="Описание привычки", help_text="Опишите, что необходимо сделать"
    )
    is_pleasant_habit = models.BooleanField(
        verbose_name="Признак приятной привычки",
        help_text="Выберите, является ли эта привычка приятной",
    )
    related_habit = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        **NULLABLE,
        verbose_name="Связанная привычка",
        help_text="Выберите приятную привычку за выполнение полезной",
    )
    period = models.PositiveIntegerField(
        default=1,
        verbose_name="Периодичность выполнения",
        help_text="Введите периуд выполнения привычки, в днях, не больше 7 дней",
    )
    award = models.TextField(
        verbose_name="Вознаграждение",
        **NULLABLE,
        help_text="Введите вознаграждение за выполнение полезной привычки",
    )
    time_to_complete = models.PositiveIntegerField(
        verbose_name="Время на выполнение привычки",
        help_text="Введите время в секундах на выполнение привычки, до 120 сек",
    )
    is_public = models.BooleanField(
        verbose_name="Признак публичной привычки",
        help_text="Выберите, является ли привычка публичной",
    )
    next_date = models.DateField(
        auto_now_add=True, verbose_name="Дата следующего выполнения"
    )

    def __str__(self):
        return f"{self.description}: {self.time} в {self.place}"

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
