# Generated by Django 3.2.12 on 2025-03-11 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_student_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='student_id',
            new_name='mat_number',
        ),
    ]
