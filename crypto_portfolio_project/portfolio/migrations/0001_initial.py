# Generated by Django 4.0.3 on 2024-03-19 12:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CryptoCurrency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('symbol', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Holding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cryptocurrency', models.CharField(max_length=100)),
                ('quantity', models.DecimalField(decimal_places=5, max_digits=20)),
                ('purchase_price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('purchase_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=100)),
                ('cryptocurrency', models.CharField(max_length=100)),
                ('symbol', models.CharField(max_length=10)),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('purchase_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('purchase_date', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Holding1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=10, max_digits=20)),
                ('purchase_price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('purchase_date', models.DateField()),
                ('cryptocurrency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.cryptocurrency')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
