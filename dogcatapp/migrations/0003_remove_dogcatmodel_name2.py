# Generated by Django 2.2.5 on 2020-01-18 21:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dogcatapp', '0002_dogcatmodel_name2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dogcatmodel',
            name='name2',
        ),
    ]