# Generated by Django 4.1.2 on 2023-01-20 17:37

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('info_details', '0004_project_delete_education'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(max_length=500), blank=True, size=None),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_name',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, size=None),
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, size=None)),
                ('company', django.contrib.postgres.fields.ArrayField(base_field=models.URLField(max_length=100), blank=True, size=None)),
                ('employment_type', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(max_length=50), blank=True, size=None)),
                ('start_date', django.contrib.postgres.fields.ArrayField(base_field=models.DateField(blank=True), size=None)),
                ('end_date', django.contrib.postgres.fields.ArrayField(base_field=models.DateField(blank=True), size=None)),
                ('description', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(max_length=500), blank=True, size=None)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skills', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), blank=True, size=None)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), blank=True, size=None)),
                ('school', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, size=None)),
                ('start_year', django.contrib.postgres.fields.ArrayField(base_field=models.URLField(max_length=4), blank=True, size=None)),
                ('end_year', django.contrib.postgres.fields.ArrayField(base_field=models.URLField(max_length=4), blank=True, size=None)),
                ('grade', django.contrib.postgres.fields.ArrayField(base_field=models.URLField(max_length=2), blank=True, size=None)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]