# Generated by Django 2.0.6 on 2018-08-18 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20180818_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='date_added',
            field=models.DateTimeField(),
        ),
    ]
