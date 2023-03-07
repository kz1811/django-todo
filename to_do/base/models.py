from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    # One-to-Many relationship
    # user can have many tasks and one task can have the one owner
    # CASCADE - if users has been deleted, tasks will be deleted too
    #

    title = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(max_length=256, null=True, blank=True)
    is_complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['is_complete']
