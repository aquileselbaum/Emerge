# Generated by Django 5.0.6 on 2024-09-14 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("report", "0002_rename_post_report"),
    ]

    operations = [
        migrations.RenameField(
            model_name="report",
            old_name="content",
            new_name="description",
        ),
        migrations.RemoveField(
            model_name="report",
            name="created_at",
        ),
        migrations.RemoveField(
            model_name="report",
            name="title",
        ),
        migrations.AddField(
            model_name="report",
            name="emergencyForMe",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="report",
            name="emergencyForSomeoneElse",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="report",
            name="location",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
