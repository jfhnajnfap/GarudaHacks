# Generated by Django 5.0.4 on 2024-07-11 13:04

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0002_room_created_by"),
    ]

    operations = [
        migrations.RenameField(
            model_name="room",
            old_name="created_by",
            new_name="user",
        ),
    ]