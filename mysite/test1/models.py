from django.db import models


class Test1(models.Model):
    title = models.CharField(max_length=50)
    img = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title
