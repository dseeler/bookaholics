# Generated by Django 3.1.5 on 2021-04-20 16:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0022_delete_ordermanager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]