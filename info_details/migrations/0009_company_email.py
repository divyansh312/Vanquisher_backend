# Generated by Django 4.1.3 on 2023-01-21 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info_details', '0008_company_company_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='email',
            field=models.EmailField(blank=True, max_length=254, unique=True),
        ),
    ]
