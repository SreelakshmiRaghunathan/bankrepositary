# Generated by Django 4.2.5 on 2023-09-25 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blogimg', models.ImageField(blank=True, upload_to='blog')),
                ('question', models.TextField()),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('galleryimg', models.ImageField(blank=True, upload_to='gallery')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('position', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='teams')),
            ],
        ),
    ]
