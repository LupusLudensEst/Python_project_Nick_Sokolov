# Generated by Django 3.1.5 on 2021-01-27 04:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Brand Name')),
                ('country', models.CharField(max_length=50, verbose_name='Country')),
            ],
            options={
                'verbose_name': 'Brand',
                'verbose_name_plural': 'Brands',
                'db_table': 'brands',
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Car Model')),
                ('generation', models.CharField(max_length=50, verbose_name='Generation')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.brand', verbose_name='Brand')),
            ],
            options={
                'verbose_name': 'Car',
                'verbose_name_plural': 'Cars',
                'db_table': 'cars',
            },
        ),
        migrations.CreateModel(
            name='CarItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('production_date', models.DateField(verbose_name='Date of Production')),
                ('color', models.CharField(max_length=50, verbose_name='Color')),
                ('transmission', models.CharField(choices=[('A', 'Automatic'), ('M', 'Manual'), ('R', 'Robot'), ('V', 'Variator')], default='A', max_length=1, verbose_name='Transmission')),
                ('vin', models.CharField(max_length=30, verbose_name='Vin')),
                ('status', models.CharField(choices=[('A', 'Available'), ('S', 'Sold'), ('R', 'Reserved'), ('O', 'Ordered')], default='A', max_length=1, verbose_name='Status')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.car', verbose_name='Car')),
            ],
            options={
                'verbose_name': 'Car Item',
                'verbose_name_plural': 'Cars Items',
                'db_table': 'cars_item',
            },
        ),
    ]
