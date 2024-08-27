from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Airport(models.Model):
    
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.city} ({self.code})"
    
class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="origen")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="destino")
    duration = models.IntegerField()

    def __str__(self):
        return f"From {self.origin} to {self.destination}"
    
# class CustomUser(AbstractUser):
#     pass
