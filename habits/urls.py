from django.urls import path

from habits.apps import HabitsConfig
from habits.views import (HabitCreateApiView, HabitDestroyApiView,
                          HabitListApiView, HabitPublicListApiView,
                          HabitRetrieveApiView, HabitUpdateApiView)

app_name = HabitsConfig.name

urlpatterns = [
    path("habits/", HabitListApiView.as_view(), name="habits_list"),
    path("habits/public", HabitPublicListApiView.as_view(), name="public_habits_list"),
    path("habits/<int:pk>/", HabitRetrieveApiView.as_view(), name="habits_retrieve"),
    path("habits/<int:pk>/update/", HabitUpdateApiView.as_view(), name="habits_update"),
    path(
        "habits/<int:pk>/delete/", HabitDestroyApiView.as_view(), name="habits_delete"
    ),
    path("habits/create/", HabitCreateApiView.as_view(), name="habits_create"),
]
