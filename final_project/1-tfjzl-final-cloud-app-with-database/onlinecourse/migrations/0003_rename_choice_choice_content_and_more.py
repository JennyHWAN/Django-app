# Generated by Django 4.2.3 on 2023-09-16 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0002_choice_submission_question_choice_question'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='choice',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='question',
            new_name='content',
        ),
    ]
