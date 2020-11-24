from django.db import models

class Solver(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)
