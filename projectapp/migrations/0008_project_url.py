# Generated by Django 2.2.5 on 2020-01-14 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0007_auto_20200114_0953'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='url',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]
