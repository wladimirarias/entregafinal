# Generated by Django 4.1.3 on 2022-12-05 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empresa',
            name='user',
        ),
    ]
