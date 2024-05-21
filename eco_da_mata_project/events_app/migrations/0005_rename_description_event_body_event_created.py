# Generated by Django 5.0.6 on 2024-05-20 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events_app', '0004_alter_event_category_alter_event_description_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='description',
            new_name='body',
        ),
        migrations.AddField(
            model_name='event',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]