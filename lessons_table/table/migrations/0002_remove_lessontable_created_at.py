# Generated by Django 3.2 on 2022-08-03 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lessontable',
            name='created_at',
        ),
    ]
