from django.db import models

# models is the name of the file and Model is the class name
class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=70)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    published_year = models.IntegerField(default=2023)
    available = models.BooleanField(default=False)


    def __str__(self):
        return f"id: {self.id} Book:{self.title} Author name: {self.title} {self.author}"



# name='Book 2',
#     ...     price=50,
#     ...     published_year=2023,
#     ...     published=None,
#     ...     available=True,
#     ...     author=author,