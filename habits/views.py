from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from habits.models import Habit
from habits.serializers import HabitSerializer


class HabitCreateApiView(CreateAPIView):
    """Создание привычки"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        """Привязываем владельца к привычке"""
        habit = serializer.save()
        habit.owner = self.request.user
        habit.save()


class HabitListApiView(ListAPIView):
    """Просмотр списка привычек"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitRetrieveApiView(RetrieveAPIView):
    """Просмотр одной привычки"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitUpdateApiView(UpdateAPIView):
    """Изменение привычки"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitDestroyApiView(DestroyAPIView):
    """Удаление привычки"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
