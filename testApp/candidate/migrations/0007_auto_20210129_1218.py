# Generated by Django 3.1.5 on 2021-01-29 12:18

import candidate.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0006_auto_20210129_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='resume',
            field=models.FileField(default='', upload_to='https://drive.google.com/drive/u/0/folders/11U8zwAntL0sPRApxPsT58_h7qJ2_KUP3/', validators=[candidate.validators.validate_file_extension]),
        ),
    ]