# Generated by Django 4.2.16 on 2024-10-14 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_application', '0002_product_food_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='uploaded_file',
            field=models.FileField(null=True, upload_to='documents/'),
        ),
    ]
