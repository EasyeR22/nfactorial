from django.db import models

# Create your models here.
class Dog(models.Model):
    name = models.TextField()
    description = models.TextField(null = True,blank=True)

    def __str__(self):
        return self.name
    