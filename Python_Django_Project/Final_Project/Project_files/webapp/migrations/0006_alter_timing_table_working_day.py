# Generated by Django 4.2.7 on 2023-12-05 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_delete_datetimerecord_alter_timing_table_break_end_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timing_table',
            name='working_day',
            field=models.DateTimeField(null=True),
        ),
    ]
