# Generated by Django 2.2.5 on 2020-01-13 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0005_project_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='main_project/'),
        ),
    ]