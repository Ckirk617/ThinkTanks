# Generated by Django 2.0.5 on 2018-07-18 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='policyarea',
            name='topic',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]