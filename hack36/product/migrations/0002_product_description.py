# Generated by Django 3.2.9 on 2022-04-23 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(default='', max_length=50),
        ),
    ]
