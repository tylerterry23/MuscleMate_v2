from django.shortcuts import render

from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import JsonResponse
from .models import Workout  # Import your model

# Create your views here.
def workout_index(request):
    return render(request, 'tracking/workout_form1.html')



def refresh_table(request):
    if request.method == 'POST':
        workouts = Workout.objects.filter(user=request.user)
        html = render_to_string('tracking/workout_table.html', {'workouts': workouts})
        return JsonResponse({'html': html}, safe=False)

def delete_workout(request):
    if request.method == 'POST':
        workout_id = request.POST.get('id')
        Workout.objects.filter(id=workout_id).delete()
        return JsonResponse({'success': True})
