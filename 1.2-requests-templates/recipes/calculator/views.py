from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}

def receipts(request, name):
    recipe = DATA.get(name, {})
    try:
        count = int(request.GET.get('servings', 1))
    except ValueError:
        count = 1
    recipe = {ingredient: count * amount for ingredient, amount in recipe.items() }
    return render(request, "calculator/index.html", { "recipe": recipe })