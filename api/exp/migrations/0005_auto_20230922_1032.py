# Generated by Django 3.0.3 on 2023-09-22 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exp', '0004_auto_20230922_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cab',
            name='carImage',
            field=models.CharField(max_length=100000, null=True),
        ),
        migrations.AlterField(
            model_name='hotels',
            name='image',
            field=models.CharField(max_length=100000, null=True),
        ),
        migrations.AlterField(
            model_name='places',
            name='pimage',
            field=models.CharField(max_length=100000, null=True),
        ),
    ]
