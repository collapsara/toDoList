from django.db import models


class Task(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField()
    deadline = models.DateTimeField()
    isDone = models.BooleanField(default=False)

    def execute(self):
        self.isDone = True

    class Meta:
        ordering = ['deadline']
