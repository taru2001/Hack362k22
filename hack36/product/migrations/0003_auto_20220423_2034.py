# Generated by Django 3.1 on 2022-04-23 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
