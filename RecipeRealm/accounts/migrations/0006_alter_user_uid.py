# Generated by Django 4.2.1 on 2023-06-15 23:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_user_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('758f6625-b70a-45e3-8a10-9cc4069279fb'), primary_key=True, serialize=False),
        ),
    ]
