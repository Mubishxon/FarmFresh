# Generated by Django 5.1.1 on 2024-11-27 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_carousel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carousel',
            name='bio',
        ),
    ]
