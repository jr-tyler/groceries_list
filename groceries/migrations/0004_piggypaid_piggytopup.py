# Generated by Django 2.1.3 on 2018-12-03 22:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('groceries', '0003_auto_20181122_1625'),
    ]

    operations = [
        migrations.CreateModel(
            name='PiggyPaid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paid_date', models.DateField(default=django.utils.timezone.now)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='piggy_paid', to='groceries.Grocery')),
            ],
        ),
        migrations.CreateModel(
            name='PiggyTopUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=200)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('added_date', models.DateField(default=django.utils.timezone.now)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]