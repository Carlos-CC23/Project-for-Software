from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Recipe
from .models import Recipe, AppointmentHistory  # Make sure to import AppointmentHistory

class AppointmentHistoryAdmin(admin.ModelAdmin):
    list_display = ('patient_name', 'created_at', 'recorded_by')
    fieldsets = (
        (None, {
            'fields': ('patient_name', 'discussion_notes', 'recorded_by')
        }),
        ('Patient Questionnaire', {
            'fields': (
                'question_1_response',
                'question_2_response',
                'question_3_response',
                'question_4_response',
                'question_5_response',
                'question_6_response',
                'question_7_response',
                'question_8_response',
            ),
            'description': 'Fill out based on patient responses.'
        }),
    )
    readonly_fields = ('recorded_by',)

    def save_model(self, request, obj, form, change):
        if not obj.recorded_by:
            obj.recorded_by = request.user
        obj.save()

class RecipeAdmin(TranslationAdmin):
    list_display = ('name', 'ingredients', 'medical_conditions', 'nutritional_info', 'cost', 'image')

admin.site.register(Recipe, RecipeAdmin)

admin.site.register(AppointmentHistory, AppointmentHistoryAdmin)
#admin.site.register(AppointmentHistory, HistoryAdmin)

