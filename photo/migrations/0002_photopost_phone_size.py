# Generated by Django 2.1.7 on 2019-05-26 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photopost',
            name='phone_size',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]