# Generated by Django 2.0.6 on 2018-08-18 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_auto_20180818_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='contact_number',
            field=models.CharField(max_length=10),
        ),
    ]
