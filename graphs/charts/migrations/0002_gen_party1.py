# Generated by Django 2.1.2 on 2018-11-05 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gen',
            name='party1',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]
