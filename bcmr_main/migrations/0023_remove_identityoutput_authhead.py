# Generated by Django 3.1.6 on 2023-06-08 01:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bcmr_main', '0022_auto_20230608_0134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='identityoutput',
            name='authhead',
        ),
    ]
