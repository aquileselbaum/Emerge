# Generated by Django 5.0.6 on 2024-09-14 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("report", "0005_report_priority"),
    ]

    operations = [
        migrations.AddField(
            model_name="report",
            name="actionResponse",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="report",
            name="suppliesResponse",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="report",
            name="priority",
            field=models.IntegerField(default=5),
        ),
    ]