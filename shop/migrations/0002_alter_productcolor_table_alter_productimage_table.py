# Generated by Django 4.1.7 on 2023-03-03 03:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='productcolor',
            table='shop_product_color',
        ),
        migrations.AlterModelTable(
            name='productimage',
            table='shop_product_image',
        ),
    ]
