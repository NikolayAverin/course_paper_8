import datetime

from celery import shared_task
from django.utils import timezone

from habits.models import Habit
from habits.services import send_tg_message


@shared_task
def send_message_about_habit():
    """Задача, проверяющая привычки на сегодня и вызывающая отправку их в телеграмм пользователя"""
    today = timezone.now().today().date()
    habits = Habit.objects.filter(next_date=today)
    for habit in habits:
        if habit.owner.telegram_id:
            send_tg_message(habit.owner.telegram_id, habit)
            print(habit)
        habit.next_date = today + datetime.timedelta(days=habit.period)
        habit.save()
