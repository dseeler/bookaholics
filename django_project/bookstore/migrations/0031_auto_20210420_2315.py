# Generated by Django 3.1.5 on 2021-04-20 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0030_order_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='time',
            field=models.TimeField(),
        ),
    ]