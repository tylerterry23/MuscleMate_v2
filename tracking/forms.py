from django import forms
from .models import Workout, Exercise, NutritionEntry, FoodServing, Meal

# Form for creating a workout
class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['date', 'duration', 'calories_burned', 'workout_type', 'notes', 'is_completed', 'rating', 'is_favorite']

# Form for creating an exercise
class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['name', 'sets', 'reps', 'weight_lbs']

# Form for creating a nutrition entry
class NutritionEntryForm(forms.ModelForm):
    class Meta:
        model = NutritionEntry
        fields = ['date', 'meal', 'notes']

# Form for creating a meal
class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ['name']

# Form for creating a food serving
class FoodServingForm(forms.ModelForm):
    class Meta:
        model = FoodServing
        fields = ['food', 'serving_size']
