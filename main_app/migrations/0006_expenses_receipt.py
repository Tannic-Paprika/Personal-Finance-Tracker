# Generated by Django 5.0.6 on 2024-05-21 06:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main_app", "0005_expenses_shared_by"),
    ]

    operations = [
        migrations.AddField(
            model_name="expenses",
            name="receipt",
            field=models.FileField(blank=True, null=True, upload_to="receipts/"),
        ),
    ]
