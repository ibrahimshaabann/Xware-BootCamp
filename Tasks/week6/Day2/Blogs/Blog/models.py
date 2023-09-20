from django.db import models
from Author.models import Author


class Post(models.Model):
    title = models.CharField(max_length=60, blank=False)
    content = models.TextField()
    publish_date = models.DateField( blank=False)
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="The author who created the blog")


    # class Meta:
    #     ordering = ['publish_date']
   

    