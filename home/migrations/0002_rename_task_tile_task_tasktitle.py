# Generated by Django 5.0.3 on 2024-06-15 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='task_tile',
            new_name='taskTitle',
        ),
    ]
