# Generated by Django 5.0.6 on 2024-09-14 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("report", "0003_rename_content_report_description_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="report",
            name="resolved",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="report",
            name="location",
            field=models.CharField(default=False, max_length=255),
            preserve_default=False,
        ),
    ]
