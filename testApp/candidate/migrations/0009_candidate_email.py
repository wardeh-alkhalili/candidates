# Generated by Django 3.1.5 on 2021-01-29 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0008_auto_20210129_1226'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='email',
            field=models.CharField(default='', max_length=300),
        ),
    ]
