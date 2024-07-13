from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class UserTestCase(APITestCase):
    """Тесты для пользователя"""

    def setUp(self):
        self.user = User.objects.create(email="test@test.com")
        self.client.force_authenticate(user=self.user)
        # self.habit = Habit.objects.create(owner=self.user, place="Test place", time="morning",
        #                                   description="Test description", is_pleasant_habit=False, time_to_complete=10,
        #                                   is_public=True)

    def test_user_register(self):
        """Регистрация пользователя"""
        url = reverse("users:user_create")
        data = {"email": "test2@test.com", "password": "111111"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(str(User.objects.get(email="test2@test.com")), "test2@test.com")

    # def test_user_owner(self):
    #     self.habit = Habit.objects.create(owner=self.user, place="Test place", time="morning",
    #                                  description="Test description", is_pleasant_habit=False, time_to_complete=10,
    #                                  is_public=True)
    #     self.new_user = User.objects.create(email="test3@test.com")
    #     self.client.force_authenticate(user=self.new_user)
    #     url = reverse("habits:habits_list")
    #     response = self.client.get(url)
    #     print(response.json())
    #     print(self.habit)
    #     self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)


