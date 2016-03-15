from django.db import models

from django.utils import timezone


class Post(models.Model):
    #To create a recursive relationship
    author = models.ForeignKey('auth.User')
    #limited number of characters
    title = models.CharField(max_length=200)
    #this is to handle text
    text = models.TextField()
    #This is to set the DateTime
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


