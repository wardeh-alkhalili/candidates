# Generated by Django 3.1.5 on 2021-01-29 12:04

import candidate.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0004_remove_candidate_is_admin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='resume_url',
        ),
        migrations.AddField(
            model_name='candidate',
            name='resume',
            field=models.FileField(default='', upload_to='documents/%Y/%m/%d', validators=[candidate.validators.validate_file_extension]),
        ),
    ]
