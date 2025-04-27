from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q, F
from .models import Recipe
from django.utils.translation import gettext as _


def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})

def recipe_list(request):
    recipe_name_query = request.GET.get('recipe_name', '') # New
    ingredient_query = request.GET.get('ingredient', '')   # New
    medical_condition = request.GET.get('medical_condition', '')

    recipes = Recipe.objects.all()

    all_conditions = Recipe.objects.exclude(medical_conditions="").values_list('medical_conditions', flat=True)
    unique_conditions = sorted({cond for cond in all_conditions if cond})
    #unique_conditions = sorted(set(all_conditions))

    if recipe_name_query:
        recipes = recipes.filter(name__icontains=recipe_name_query) # Filter by name

    #if ingredient_query:
       # recipes = recipes.filter(ingredients__icontains=ingredient_query)

    if medical_condition:
        recipes = recipes.filter(medical_conditions__icontains=medical_condition)

    # 4) Paginate
    paginator = Paginator(recipes, 9)
    page_obj = paginator.get_page(request.GET.get('page'))

  
    # 6) Render
    return render(request, 'recipes/recipe_list.html', {
        'page_obj': page_obj,
        'medical_conditions': unique_conditions,
    })

def calculate_calories(request):
    # Redirect GETs back to list
    if request.method != 'POST':
        return redirect('recipe_list')

    # 1) Pull form data
    gender       = request.POST.get('gender')
    height_raw   = request.POST.get('height')
    weight_raw   = request.POST.get('weight')
    age_raw      = request.POST.get('age')
    activity_raw = request.POST.get('activity_level', 1.2)
    goal         = request.POST.get('goal')

    error = None
    results = {}
    form_data = {
        'gender': gender,
        'height': height_raw,
        'weight': weight_raw,
        'age': age_raw,
        'activity_level': activity_raw,
        'goal': goal,
    }

    # 2) Compute BMR / TDEE / macros
    try:
        height       = float(height_raw)
        weight       = float(weight_raw)
        age          = float(age_raw)
        activity_lvl = float(activity_raw)

        if height <= 0 or weight <= 0 or age <= 0:
            raise ValueError

        # Mifflin–St Jeor
        if gender == 'male':
            bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
        else:
            bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161

        tdee = bmr * activity_lvl

        if goal == 'loss':
            rec = tdee - 500
        elif goal == 'gain':
            rec = tdee + 300
        else:
            rec = tdee

        results = {
            'bmr': round(bmr),
            'tdee': round(tdee),
            'recommended_calories': round(rec),
            'protein_grams': round((rec * 0.3)   / 4),
            'carbs_grams':   round((rec * 0.4)   / 4),
            'fat_grams':     round((rec * 0.3)   / 9),
        }
    except (ValueError, TypeError):
        error = _("Please enter valid numeric values for height, weight, and age.")

    recipe_name_query = request.GET.get('recipe_name', '') # New
    ingredient_query = request.GET.get('ingredient', '')   # New
    medical_condition = request.GET.get('medical_condition', '')

    recipes = Recipe.objects.all()

    all_conditions = Recipe.objects.exclude(medical_conditions="").values_list('medical_conditions', flat=True)
    unique_conditions = sorted({cond for cond in all_conditions if cond})
    #unique_conditions = sorted(set(all_conditions))

    if recipe_name_query:
        recipes = recipes.filter(name__icontains=recipe_name_query) # Filter by name

    #if ingredient_query:
       # recipes = recipes.filter(ingredients__icontains=ingredient_query)

    if medical_condition:
        recipes = recipes.filter(medical_conditions__icontains=medical_condition)

    # 4) Paginate
    paginator = Paginator(recipes, 9)
    page_obj = paginator.get_page(request.GET.get('page'))

      
    # 5) Render back into list template
    return render(request, 'recipes/recipe_list.html', {
        'page_obj':           page_obj,
        'medical_conditions': unique_conditions,
        'error':              error,
        'has_results':        bool(results),
        'results':            results,
        'form_data':          form_data,
    })
