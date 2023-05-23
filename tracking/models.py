'''
Tracking models:
This section focuses on fitness and nutrition tracking functionalities. 
The WorkoutType, Workout, and Exercise models handle workout related data. 
Each workout is linked to a user and a type of workout and can have multiple exercises. 
The Food, NutritionPlan, Meal, and FoodServing models handle dietary tracking.
Users can create food items with nutritional data, which can then be included in meals as part of a nutrition plan. 
Finally, the Goal, ProgressPhoto, and Measurement models are for tracking general progress towards fitness goals.
'''
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

from users.models import Profile

# Section: Workout
class WorkoutType(models.Model):
    name = models.CharField(max_length=100)
    created_by = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    body_part_choices = [ 
        ('CORE', 'Core'),
        ('ARMS', 'Arms'),
        ('BACK', 'Back'),
        ('CHEST', 'Chest'),
        ('LEGS', 'Legs'),
        ('SHOULDERS', 'Shoulders'),
        ('OTHER', 'Other'),
        ('OLYMPIC', 'Olympic'),
        ('FULL_BODY', 'Full Body'),
        ('CARDIO', 'Cardio'),
    ]
    body_part = models.CharField(max_length=20, choices=body_part_choices)
    category_choices = [
        ('BARBELL', 'Barbell'),
        ('DUMBBELL', 'Dumbbell'),
        ('MACHINE', 'Machine / Other'),
        ('WEIGHTED_BODYWEIGHT', 'Weighted Bodyweight'),
        ('ASSISTED_BODYWEIGHT', 'Assisted Bodyweight'),
        ('CARDIO', 'Cardio'),
        ('DURATION', 'Duration'),
    ]
    category = models.CharField(max_length=20, choices=category_choices)
    description = models.TextField()
    image = models.ImageField(upload_to='workout_type_images/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Workout Types'

class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    updated_at = models.DateTimeField(auto_now=True)
    duration = models.PositiveIntegerField()
    calories_burned = models.PositiveIntegerField()
    workout_type = models.ForeignKey(WorkoutType, on_delete=models.CASCADE)
    notes = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)
    rating = models.PositiveIntegerField(null=True, blank=True)
    is_favorite = models.BooleanField(default=False)
    likes = models.ManyToManyField(Profile, related_name='liked_workouts', blank=True)
    shares = models.ManyToManyField(Profile, related_name='shared_workouts', blank=True)
    comments = models.ManyToManyField('social.Comment', blank=True)
    rating = models.PositiveIntegerField(null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(5)])


    def __str__(self):
        return f"Workout on {self.date}"

    class Meta:
        ordering = ['-date']

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    created_by = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    sets = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    reps = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    weight_lbs = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0)])
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name='exercises')
    likes = models.ManyToManyField(Profile, related_name='liked_exercises', blank=True)
    shares = models.ManyToManyField(Profile, related_name='shared_exercises', blank=True)
    comments = models.ManyToManyField('social.Comment', blank=True)

    def __str__(self):
        return self.name


# Section: Nutrition
class Food(models.Model):
    name = models.CharField(max_length=100)
    created_by = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    calories = models.PositiveIntegerField()
    carbohydrates = models.PositiveIntegerField()
    proteins = models.PositiveIntegerField()
    fats = models.PositiveIntegerField()
    likes = models.ManyToManyField(Profile, related_name='liked_foods', blank=True)
    shares = models.ManyToManyField(Profile, related_name='shared_foods', blank=True)
    comments = models.ManyToManyField('social.Comment', blank=True)

    def __str__(self):
        return self.name

class NutritionPlan(models.Model):
    name = models.CharField(max_length=100)
    created_by = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    likes = models.ManyToManyField(Profile, related_name='liked_nutrition_plans', blank=True)
    shares = models.ManyToManyField(Profile, related_name='shared_nutrition_plans', blank=True)
    comments = models.ManyToManyField('social.Comment', blank=True)

    
    def __str__(self):
        return self.name

class Meal(models.Model):
    name = models.CharField(max_length=100)
    foods = models.ManyToManyField(Food, through='FoodServing')

    def __str__(self):
        return self.name

class FoodServing(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    serving_size = models.PositiveIntegerField(verbose_name='Serving Size')

    def __str__(self):
        return f"Serving of {self.food.name} for {self.meal.name}"

class NutritionEntry(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date = models.DateField()
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Nutrition Entry for {self.user.username} on {self.date}"

    class Meta:
        ordering = ['-date']


# Section: Other
class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    deadline = models.DateField()
    STATUS_CHOICES = [
        ('O', 'Ongoing'),
        ('A', 'Achieved'),
        ('F', 'Failed'),
    ]
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='O')

class ProgressPhoto(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    photo = models.ImageField(upload_to='progress_photos/')
    notes = models.TextField(blank=True)
    likes = models.ManyToManyField(Profile, related_name='liked_progress_photos', blank=True)
    shares = models.ManyToManyField(Profile, related_name='shared_progress_photos', blank=True)
    comments = models.ManyToManyField('social.Comment', blank=True)

    def __str__(self):
        return f"Progress Photo for {self.user.username} on {self.date}"

    class Meta:
        ordering = ['-date']

class Measurement(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    MEASUREMENT_TYPE_CHOICES = [
        ('W', 'Weight'),
        ('H', 'Height'),
        # Add more measurement types here...
    ]
    updated_at = models.DateTimeField(auto_now=True)
    measurement_type = models.CharField(max_length=1, choices=MEASUREMENT_TYPE_CHOICES)
    value = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"Measurement for {self.user.username} on {self.date}"

    class Meta:
        ordering = ['-date']

