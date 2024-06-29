from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from habits.models import Habit
from habits.serializers import HabitSerializer


class HabitCreateApiView(CreateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        """Привязываем владельца к привычке"""
        habit = serializer.save()
        habit.owner = self.request.user
        habit.save()


class HabitListApiView(ListAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitRetrieveApiView(RetrieveAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitUpdateApiView(UpdateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitDestroyApiView(DestroyAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
