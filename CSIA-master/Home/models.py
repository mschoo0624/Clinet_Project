from pyexpat import model
from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=25)
    mobile = models.CharField(max_length=15)
    position = models.CharField(max_length=12)
    dob = models.DateField()
    nationality = models.CharField(max_length=30)
    p_id = models.IntegerField(primary_key=True)

    def __str__(self):
        return f"{self.name} {self.mobile}"

