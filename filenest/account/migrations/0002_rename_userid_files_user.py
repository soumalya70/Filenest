# Generated by Django 5.0.1 on 2024-01-11 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(model_name="files", old_name="Userid", new_name="User",),
    ]
