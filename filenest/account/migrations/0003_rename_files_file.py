# Generated by Django 5.0.1 on 2024-01-11 18:53

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0002_rename_userid_files_user"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(old_name="Files", new_name="File",),
    ]