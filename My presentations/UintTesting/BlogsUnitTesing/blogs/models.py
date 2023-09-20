from django.db import models
from django.contrib.auth.models import User    

class Author(models.Model):
    email = models.EmailField(max_length=255,blank=False)
    name = models.CharField(max_length=20 , blank=False)
    age = models.SmallIntegerField()

    def __str__(self) :
        return f"{self.user.username}"
   

class Post(models.Model):
    title = models.CharField(max_length=60, blank=False)
    content = models.TextField()
    creationDate = models.DateTimeField( blank=False, auto_now_add=True)
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="The author who created the blog")

    def __str__(self) :
        return f"{self.title} {self.creationDate}"