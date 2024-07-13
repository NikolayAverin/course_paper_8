from django.urls import path

from habits.apps import HabitsConfig
from habits.views import (HabitCreateApiView, HabitDestroyApiView,
                          HabitListApiView, HabitPublicListApiView,
                          HabitRetrieveApiView, HabitUpdateApiView)

app_name = HabitsConfig.name

urlpatterns = [
    path("list/", HabitListApiView.as_view(), name="habits_list"),
    path("public/", HabitPublicListApiView.as_view(), name="public_habits_list"),
    path("<int:pk>/", HabitRetrieveApiView.as_view(), name="habits_retrieve"),
    path("<int:pk>/update/", HabitUpdateApiView.as_view(), name="habits_update"),
    path(
        "<int:pk>/delete/", HabitDestroyApiView.as_view(), name="habits_delete"
    ),
    path("create/", HabitCreateApiView.as_view(), name="habits_create"),
]
