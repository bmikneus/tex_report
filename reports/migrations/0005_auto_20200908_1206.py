# Generated by Django 3.1.1 on 2020-09-08 17:06

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0004_report_other'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='problem',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Eyes', 'Eyes'), ('Mouth', 'Mouth'), ('Wrist', 'Wrist'), ('Hand', 'Hand'), ('Arm', 'Arm'), ('Forearm', 'Forearm'), ('Neck', 'Neck'), ('Nod', 'Nod'), ('Message', 'Message'), ('Other', 'Other')], max_length=56),
        ),
    ]
