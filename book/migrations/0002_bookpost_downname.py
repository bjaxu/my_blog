# Generated by Django 2.1.7 on 2019-05-20 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookpost',
            name='downname',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
