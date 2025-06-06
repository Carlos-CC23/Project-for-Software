# Generated by Django 5.1.6 on 2025-04-24 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_recipe_views'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='views',
        ),
        migrations.AddField(
            model_name='recipe',
            name='cost',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='cost_en',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='cost_es',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients_es',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='medical_conditions_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='medical_conditions_es',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='name_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='name_es',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='nutritional_info_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='nutritional_info_es',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='preparation_steps_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='preparation_steps_es',
            field=models.TextField(null=True),
        ),
    ]
