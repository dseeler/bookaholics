# Generated by Django 3.1.5 on 2021-04-14 02:35

from django.db import migrations, models
import django_cryptography.fields


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0011_auto_20210414_0234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='card_code',
            field=django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=3, null=True)),
        ),
        migrations.AlterField(
            model_name='user',
            name='card_exp',
            field=django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=5, null=True)),
        ),
        migrations.AlterField(
            model_name='user',
            name='card_num',
            field=django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=16, null=True)),
        ),
    ]
