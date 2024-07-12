from rest_framework.serializers import ModelSerializer
from habits.models import Habit
from habits.validators import TimeToCompleteValidator, RelatedHabitValidator, IsPleasantHabitValidator, AwardValidator


class HabitSerializer(ModelSerializer):
    """Сериализатор привычки"""

    class Meta:
        model = Habit
        fields = "__all__"
        validators = [TimeToCompleteValidator(field='time_to_complete'), RelatedHabitValidator(field="related_habit"), IsPleasantHabitValidator(is_pleasant_habit="is_pleasant_habit", award="award", related_habit="related_habit"), AwardValidator(award="award", related_habit="related_habit")]
