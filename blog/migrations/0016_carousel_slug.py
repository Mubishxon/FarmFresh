# Generated by Django 5.1.1 on 2024-11-29 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_alter_blog_span'),
    ]

    operations = [
        migrations.AddField(
            model_name='carousel',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
