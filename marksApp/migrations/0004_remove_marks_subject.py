# Generated by Django 3.1.7 on 2021-07-18 04:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marksApp', '0003_remove_marksrecord_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marks',
            name='Subject',
        ),
    ]