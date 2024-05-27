# blog/models.py
from django.db import models

class Engineer(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} - {self.position}'
    


class Task(models.Model):
    name = models.CharField(max_length=100)
    time_machine_1 = models.IntegerField()
    time_machine_2 = models.IntegerField()

    def __str__(self):
        return self.name

