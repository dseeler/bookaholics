# Generated by Django 3.1.5 on 2021-04-15 23:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0014_cartitem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='bookID',
            new_name='book',
        ),
        migrations.RenameField(
            model_name='cartitem',
            old_name='cartID',
            new_name='cart',
        ),
    ]
