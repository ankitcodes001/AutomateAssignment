from django.db import models

# Create your models here.
class Users (models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=30)
    
    def __str__(self) -> str:
        return self.name