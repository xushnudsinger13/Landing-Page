# Generated by Django 4.1 on 2022-09-14 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_portfoliostype_portfoliotitle_portfolios'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolios',
            name='name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
