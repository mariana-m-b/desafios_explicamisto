# Generated by Django 5.0 on 2023-12-27 23:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_explicamisto', '0012_user_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='explicador',
            name='user',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]