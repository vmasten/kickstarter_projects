# Generated by Django 2.1.5 on 2019-01-17 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_data', '0013_project_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='country',
            field=models.CharField(default='US', max_length=64),
        ),
    ]