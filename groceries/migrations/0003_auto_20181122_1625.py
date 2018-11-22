# Generated by Django 2.1.3 on 2018-11-22 03:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('groceries', '0002_auto_20181121_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grocery',
            name='bought_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='grocery',
            name='paid_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
