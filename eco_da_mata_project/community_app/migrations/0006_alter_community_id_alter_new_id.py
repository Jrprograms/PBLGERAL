# Generated by Django 5.0.6 on 2024-05-18 18:26

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community_app', '0005_alter_community_id_alter_new_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='new',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]