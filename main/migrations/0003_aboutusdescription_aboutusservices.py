# Generated by Django 4.1 on 2022-09-14 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_mainmenu_icon_first_mainmenu_icon_second'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutusDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('minitext', models.CharField(max_length=255)),
                ('basictext', models.CharField(max_length=255)),
                ('img', models.ImageField(upload_to='aboutdescription/')),
            ],
        ),
        migrations.CreateModel(
            name='AboutusServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titleservices', models.CharField(max_length=255)),
                ('textservices', models.TextField()),
            ],
        ),
    ]
