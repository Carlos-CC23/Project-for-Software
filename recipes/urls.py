from django.urls import path
from .views import recipe_list, recipe_detail, calculate_calories
from . import views # for the appointments add and list

urlpatterns = [
    path('', recipe_list, name='recipe_list'),
    path('<int:recipe_id>/', recipe_detail, name='recipe_detail'),
    path('calculate-calories/', calculate_calories, name='calculate_calories'),
    ]
