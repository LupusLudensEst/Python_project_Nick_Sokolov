# Generated by Django 3.1.4 on 2020-12-30 00:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products5_1', '0005_auto_20201229_1912'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='priceeee',
            new_name='price',
        ),
    ]