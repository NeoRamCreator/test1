# Generated by Django 3.2.8 on 2021-11-30 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('w2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
