# Generated by Django 4.2 on 2023-04-04 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobs',
            name='subcategory',
        ),
    ]
