# Generated by Django 4.1 on 2022-09-14 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_navbars_officiallink'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormFooter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
    ]
