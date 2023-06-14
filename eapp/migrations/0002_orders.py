# Generated by Django 4.1 on 2023-04-05 03:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(default=1)),
                ('razorpay_pid', models.CharField(default='NULL', max_length=500)),
                ('razorpay_oid', models.CharField(default='NULL', max_length=500)),
                ('razorpay_sign', models.CharField(default='NULL', max_length=500)),
                ('ispaid', models.BooleanField(default=False)),
                ('myuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eapp.product')),
            ],
        ),
    ]