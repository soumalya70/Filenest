# Generated by Django 5.0.1 on 2024-01-12 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0005_alter_file_file"),
    ]

    operations = [
        migrations.AlterField(
            model_name="file",
            name="file",
            field=models.FileField(upload_to="uploads/"),
        ),
    ]
