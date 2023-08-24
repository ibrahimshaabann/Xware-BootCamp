from django.db import models

# models is the name of the file and Model is the class name
class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=70)
    isbn = models.IntegerField()

    def __str__(self):
        return f"id: {self.id} Book:{self.title} Author name: {self.title} {self.author}"


