from django.db import models
from django.urls import reverse


class Person(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField(blank=True, null=True)
    img = models.ImageField(blank=True, null=True)
    price = models.PositiveIntegerField(null=True, blank=True, default='0')

    def __str__(self):
        return self.title

    # def a_order_by(self):
    #     return Person.objects.order_by('title')
    #
    # @property
    # def sorted_attendee_set(self):
    #     return self.person_set.order_by('title')

    # def get_absolute_url(self):
    #     return reverse('user', kwargs={'pk': self.pk})
