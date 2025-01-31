# Generated by Django 5.1.1 on 2024-11-25 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_polizekinlari_delete_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('bio', models.TextField()),
                ('price', models.IntegerField()),
                ('img', models.ImageField(upload_to='about/')),
            ],
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('bio', models.TextField()),
                ('price', models.IntegerField()),
                ('img', models.ImageField(upload_to='banner/')),
            ],
        ),
        migrations.CreateModel(
            name='Facts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('bio', models.TextField()),
                ('price', models.IntegerField()),
                ('img', models.ImageField(upload_to='facts/')),
            ],
        ),
        migrations.DeleteModel(
            name='Fermer',
        ),
        migrations.DeleteModel(
            name='Polizekinlari',
        ),
        migrations.DeleteModel(
            name='Sabzavotlar',
        ),
    ]
