from django.db import models
# Create your models here.


class Task(models.Model):
    id = models.IntegerField()
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField()
    deadline = models.DateTimeField()
    isDone = models.BooleanField(default=False)

    class Meta:
        ordering = ['deadline']