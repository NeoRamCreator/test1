# Generated by Django 3.2.8 on 2021-12-11 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('w2', '0003_alter_person_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='price',
            field=models.PositiveIntegerField(blank=True, default='', null=True),
        ),
    ]
