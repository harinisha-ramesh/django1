# Generated by Django 4.2.16 on 2024-10-07 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_application', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='food_product',
            field=models.BooleanField(default=False),
        ),
    ]
