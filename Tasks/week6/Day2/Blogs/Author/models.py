from django.db import models

class Author(models.Model):
    email = models.EmailField(max_length=255,blank=False)
    fname = models.CharField(max_length=20 , blank=False)
    lname = models.CharField(max_length=20 , blank=False)
   

# Create your models here.
