# Generated by Django 4.2.7 on 2023-12-05 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_alter_timing_table_working_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timing_table',
            name='working_day',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
