# Generated by Django 2.1.5 on 2019-01-17 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_data', '0010_auto_20190116_1720'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='name',
        ),
        migrations.AddField(
            model_name='project',
            name='category',
            field=models.CharField(default='cat', max_length=64),
        ),
    ]