# Generated by Django 3.2.8 on 2021-12-07 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='название')),
                ('num', models.PositiveIntegerField(default=0, verbose_name='номер')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='цена')),
            ],
        ),
    ]
