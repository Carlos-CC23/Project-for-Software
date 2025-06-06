# Generated by Django 5.1.6 on 2025-03-04 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('ingredients', models.TextField()),
                ('medical_conditions', models.TextField(blank=True, null=True)),
                ('preparation_steps', models.TextField()),
                ('image', models.ImageField(upload_to='recipe_images/')),
            ],
        ),
    ]
