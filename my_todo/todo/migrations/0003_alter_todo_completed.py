# Generated by Django 4.0.2 on 2022-02-19 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_rename_completed_date_todo_completed_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='completed',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
