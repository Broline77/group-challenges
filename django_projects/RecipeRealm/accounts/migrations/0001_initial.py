# Generated by Django 4.2.1 on 2023-06-01 16:53

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('uid', models.UUIDField(default=uuid.UUID('20157f0e-adb9-43a9-80ed-4905df717355'), primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='Email')),
                ('alias', models.CharField(max_length=18, unique=True, validators=[django.core.validators.RegexValidator('^[a-zA-Z0-9_]{3,18}$', message="Username should be between 3-18 characters, and must contain letters, numbers, or '_' only.")], verbose_name='Username')),
                ('full_name', models.CharField(max_length=255, null=True, verbose_name='Full name')),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('date_joined', models.DateField(auto_now_add=True)),
                ('last_login', models.DateField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
