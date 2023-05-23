from django.contrib import admin
from .models import WorkoutType, Workout, Exercise, Food, NutritionPlan, Meal, FoodServing, NutritionEntry, Goal, ProgressPhoto, Measurement

@admin.register(WorkoutType)
class WorkoutTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'body_part', 'category', 'created_by')
    list_filter = ('body_part', 'category', 'created_by')

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'workout_type', 'duration', 'calories_burned', 'is_completed')
    list_filter = ('date', 'workout_type', 'is_completed', 'user')

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('name', 'workout', 'sets', 'reps', 'weight_lbs', 'created_by')
    list_filter = ('workout', 'created_by')

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'calories', 'carbohydrates', 'proteins', 'fats', 'created_by')
    search_fields = ('name',)
    list_filter = ('calories', 'created_by')

@admin.register(NutritionPlan)
class NutritionPlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_by', 'user')
    search_fields = ('name', 'created_by__user__username', 'user__username')

@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(FoodServing)
class FoodServingAdmin(admin.ModelAdmin):
    list_display = ('food', 'meal', 'serving_size')

@admin.register(NutritionEntry)
class NutritionEntryAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'meal')
    list_filter = ('date', 'meal', 'user')

@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ('user', 'description', 'deadline', 'status')
    list_filter = ('deadline', 'status', 'user')

@admin.register(ProgressPhoto)
class ProgressPhotoAdmin(admin.ModelAdmin):
    list_display = ('user', 'date')
    list_filter = ('date', 'user')

@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ('user', 'measurement_type', 'value', 'date')
    list_filter = ('measurement_type', 'date', 'user')
