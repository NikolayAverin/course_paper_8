from rest_framework.serializers import ValidationError


class AwardValidator:
    """Исключение одновременного выбора связанной привычки и вознаграждения"""
    def __init__(self, award, related_habit):
        self.award = award
        self.related_habit = related_habit

    def __call__(self, value):
        tmp_award = dict(value).get(self.award)
        tmp_related_habit = dict(value).get(self.related_habit)
        if tmp_award and tmp_related_habit:
            raise ValidationError('Нельзя одновременно выбирать связанную привычку и вознаграждение')


class TimeToCompleteValidator:
    """Проверка на время выполнения привычки"""
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_value = dict(value).get(self.field)
        if tmp_value > 120:
            raise ValidationError(f'Время на выполнение привычки не может превышать 120 секунд')


class RelatedHabitValidator:
    """Проверка на приятность связанной привычки"""
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_related_habit = dict(value).get(self.field)
        if tmp_related_habit:
            if not tmp_related_habit.is_pleasant_habit:
                raise ValidationError('Связанная привычка должна быть приятной')


class IsPleasantHabitValidator:
    """Проверка на отсутствие связанных привычек или вознаграждения у приятной привычки"""
    def __init__(self, is_pleasant_habit, award, related_habit):
        self.is_pleasant_habit = is_pleasant_habit
        self.award = award
        self.related_habit = related_habit

    def __call__(self, value):
        tmp_is_pleasant_habit = dict(value).get(self.is_pleasant_habit)
        if tmp_is_pleasant_habit and (self.related_habit or self.award):
            raise ValidationError('Если привычка приятная, не может быть связанных привычек или вознаграждения')
