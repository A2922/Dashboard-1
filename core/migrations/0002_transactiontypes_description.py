# Generated by Django 5.1.2 on 2024-10-15 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactiontypes',
            name='description',
            field=models.TextField(default='empty'),
        ),
    ]
