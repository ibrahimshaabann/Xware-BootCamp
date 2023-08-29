from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=70)
    age = models.IntegerField()
    department = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name}  {self.department} {str(self.age)}"

# Create your models here.
