# Generated by Django 4.1.2 on 2023-01-21 07:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('info_details', '0009_company_email'),
    ]

    operations = [
        
        
        migrations.CreateModel(
            name='test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specs', models.FileField(upload_to='specs')),
            ],
        ),
       
      
    ]
