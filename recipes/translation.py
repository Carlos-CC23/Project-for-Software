# recipes/translation.py
from modeltranslation.translator import register, TranslationOptions
from .models import Recipe # Import your Recipe model

@register(Recipe)
class RecipeTranslationOptions(TranslationOptions):
    fields = ('name', 'ingredients', 'medical_conditions', 'preparation_steps', 'nutritional_info', 'cost')
    # Note: 'cost' and 'image' are generally not translated text fields.
    # 'cost' might need localization instead of translation depending on its use.
    # 'image' fields are supported by modeltranslation 0.4+ if you need different images per language.