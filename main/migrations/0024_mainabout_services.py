# Generated by Django 4.1 on 2022-09-18 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_mainabout_delete_aboutusdescription_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainabout',
            name='services',
            field=models.ManyToManyField(to='main.aboutusservices'),
        ),
    ]
