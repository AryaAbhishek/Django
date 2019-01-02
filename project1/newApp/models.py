from django.db import models

# Create your models here.
class User(models.Model):
    FirstName = models.CharField(max_length = 65)
    LastName = models.CharField(max_length = 65)
    Email = models.EmailField(max_length = 255, unique = True)
