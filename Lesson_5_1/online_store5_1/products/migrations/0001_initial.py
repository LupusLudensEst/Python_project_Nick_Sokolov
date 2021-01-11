# Generated by Django 3.1.4 on 2021-01-06 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(editable=False, max_length=30, verbose_name='Category')),
                ('description', models.TextField(editable=False, max_length=999, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(editable=False, max_length=50, verbose_name='Product name')),
                ('product_brand', models.CharField(editable=False, max_length=40, verbose_name='Product brand')),
                ('year_of_manufacture', models.IntegerField(verbose_name='Year of manufacture')),
                ('color', models.CharField(editable=False, max_length=25, verbose_name='Color')),
                ('description', models.TextField(editable=False, max_length=999, verbose_name='Description')),
                ('price', models.FloatField(editable=False, verbose_name='Price')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category', verbose_name='Category')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Product category',
                'verbose_name_plural': 'Product categories',
                'db_table': 'products_categories',
            },
        ),
    ]