# Generated by Django 3.1.1 on 2020-09-01 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0003_auto_20200901_1707'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='other',
            field=models.CharField(default='', max_length=50, null=True),
        ),
    ]