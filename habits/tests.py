from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitsTestCase(APITestCase):
    """Тесты для привычки"""

    def setUp(self):
        self.user = User.objects.create(email="test@test.com")
        self.habit = Habit.objects.create(owner=self.user, place="Test place", time="morning",
                                          description="Test description", is_pleasant_habit=False, time_to_complete=10,
                                          is_public=True)
        self.client.force_authenticate(user=self.user)

    def test_habit_create(self):
        """Создание привычки"""
        url = reverse("habits:habits_create")
        data = {
            "place": "New test place",
            "time": "evening",
            "description": "New test description",
            "is_pleasant_habit": False,
            "time_to_complete": 60,
            "is_public": False,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.count(), 2)
        self.assertEqual(str(Habit.objects.get(place="Test place")), "Test description: morning в Test place")

    def test_habit_list(self):
        """Список привычек"""
        url = reverse("habits:habits_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()["results"]), 1)

    def test_habit_retrieve(self):
        """Получение привычки по ID"""
        url = reverse("habits:habits_retrieve", args=(self.habit.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["id"], self.habit.id)

    def test_habit_update(self):
        """Обновление привычки"""
        url = reverse("habits:habits_update", args=(self.habit.id,))
        data = {"place": "Updated test place"}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["place"], "Updated test place")

    def test_habit_delete(self):
        """Удаление привычки"""
        url = reverse("habits:habits_delete", args=(self.habit.id,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.count(), 0)


class ValidatorsTestCase(APITestCase):
    """Тесты для валидаторов"""
    def setUp(self):
        self.user = User.objects.create(email="test@test.com")
        self.client.force_authenticate(user=self.user)
        self.habit = Habit.objects.create(id=1, owner=self.user, place="Test place", time="morning",
                                          description="Test description", is_pleasant_habit=False, time_to_complete=10,
                                          is_public=True)

    def test_time_to_complete_validator(self):
        """Проверка на время выполнения"""
        url = reverse("habits:habits_create")
        data = {
            "place": "New test place",
            "time": "evening",
            "description": "New test description",
            "is_pleasant_habit": False,
            "time_to_complete": 150,
            "is_public": False,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_award_validator(self):
        """Проверка на одновременный выбор вознаграждения и приятной привычки"""
        url = reverse("habits:habits_create")
        data = {
            "place": "New test place",
            "time": "evening",
            "description": "New test description",
            "is_pleasant_habit": False,
            "time_to_complete": 10,
            "is_public": False,
            "award": "Test award",
            "related_habit": 1,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_period_validator(self):
        """Проверка на допустимый период выполнения привычки"""
        url = reverse("habits:habits_create")
        data = {
            "place": "New test place",
            "time": "evening",
            "description": "New test description",
            "is_pleasant_habit": False,
            "time_to_complete": 10,
            "is_public": False,
            "period": 9,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_is_pleasant_habit_validator(self):
        """Проверка на отсутствие связанных привычек или вознаграждения у приятной привычки"""
        url = reverse("habits:habits_create")
        data = {
            "place": "New test place",
            "time": "evening",
            "description": "New test description",
            "is_pleasant_habit": True,
            "time_to_complete": 10,
            "is_public": False,
            "award": "Test award",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
