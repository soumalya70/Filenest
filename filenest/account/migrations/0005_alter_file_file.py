# Generated by Django 5.0.1 on 2024-01-12 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0004_file_file_type_file_updated_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="file",
            name="file",
            field=models.FileField(upload_to="media/uploads"),
        ),
    ]