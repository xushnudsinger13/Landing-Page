# Generated by Django 4.1 on 2022-09-14 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_formfooter'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogoImg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='logos/')),
            ],
        ),
    ]
