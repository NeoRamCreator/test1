from django.db import models


class Test2(models.Model):
    title = models.CharField('название', max_length=50)
    num = models.PositiveIntegerField('номер', default=1)
    price = models.PositiveIntegerField('цена', default=1)

    # img = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title


class Test1(models.Model):
    title = models.CharField(max_length=50)
    img = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title
