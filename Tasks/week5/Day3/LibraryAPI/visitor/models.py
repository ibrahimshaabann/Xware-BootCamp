from django.db import models

class Visitor(models.Model):
    fName = models.CharField(max_length=30)
    lName = models.CharField(max_length=30)
    email = models.CharField(max_length=130) 
    date = models.DateField()

    def __str__(self):
        return f"id: {self.id} Name: {self.fName} {self.lName}"

