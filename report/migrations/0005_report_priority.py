# Generated by Django 5.0.6 on 2024-09-14 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("report", "0004_report_resolved_alter_report_location"),
    ]

    operations = [
        migrations.AddField(
            model_name="report",
            name="priority",
            field=models.IntegerField(default=0),
        ),
    ]
