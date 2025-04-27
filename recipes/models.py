from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.TextField()
    medical_conditions = models.TextField(blank=True, null=True)
    preparation_steps = models.TextField()
    nutritional_info = models.TextField(blank=True, null=True)
    cost = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to="recipe_images/", blank=True, null=True)

    def __str__(self):
        return self.name

class AppointmentHistory(models.Model):
    patient_name = models.CharField(max_length=100)
    discussion_notes = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    recorded_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    # --- Questionnaire responses ---
    question_1_response = models.TextField(blank=True, null=True, help_text="Do you follow any specific diet? (e.g., vegetarian, keto, gluten-free)")
    question_2_response = models.TextField(blank=True, null=True, help_text="Any allergies or restrictions?")
    question_3_response = models.TextField(blank=True, null=True, help_text="Are you open to recipe substitutions?")
    question_4_response = models.TextField(blank=True, null=True, help_text="Are you currently taking any medication that affects your appetite or digestion?")
    question_5_response = models.TextField(blank=True, null=True, help_text="How active are you during the week? (sedentary, lightly active, very active)")
    question_6_response = models.TextField(blank=True, null=True, help_text="What are your current health or diet goals? (e.g., weight loss, muscle gain, healthier eating)")
    question_7_response = models.TextField(blank=True, null=True, help_text="How many meals do you typically eat in a day?")
    question_8_response = models.TextField(blank=True, null=True, help_text="Have you been diagnosed with any medical conditions that affect your diet? (e.g., diabetes, hypertension)")

    def __str__(self):
        return f"{self.patient_name} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"