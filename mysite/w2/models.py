from django.db import models
from django.urls import reverse


class Person(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField(blank=True, null=True)
    img = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('user', kwargs={'pk': self.pk})
