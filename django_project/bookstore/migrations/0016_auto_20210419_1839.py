# Generated by Django 3.1.5 on 2021-04-19 18:39

from django.db import migrations, models
import django_cryptography.fields


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0015_auto_20210415_2309'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='card_name',
            field=django_cryptography.fields.encrypt(models.CharField(blank=True, default='Default', max_length=255, null=True)),
        ),
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.CharField(blank=True, default='USA', max_length=255, null=True),
        ),
    ]