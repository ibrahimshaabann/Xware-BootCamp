## {{In our example, we'll create a library project with three tables: Book, Author, and Reader, and use ORM to interact with the database.}}

<Create models.py>

```sql
from django.db import models
from django.db.models.query import QuerySet


class Author(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()

class Book(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    published_year = models.IntegerField()
    published = models.DateField(null=True)
    available = models.BooleanField(default=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    class Meta: 
        ordering = ['name'] #order by name in ascending order, ['-name'] means descending order


class BookDetail(models.Model):
    language = models.CharField(max_length=100)
    page_count = models.IntegerField()
    book = models.OneToOneField(Book, on_delete=models.CASCADE)
class Reader(models.Model):
    name = models.CharField(max_length=100)
    borrowed_books = models.ManyToManyField(Book)


'''
Manager class is an interface that provides some functions between
is responsible for sending objects to database and getting objects from database
and turn it to python objects
'''
class AvailableBookManager(models.Manager): 
    
>> Any list you will your return from database will be returned only if its available attribute = true in book class Overriding function get_queryset in Manager class
>>> 
    def get_queryset(self) -> QuerySet:
        return super().get_queryset()  # Query set is the returned list of objecs 
```

<<Migrations>>
python manage.py makemigrations
python manage.py migrate
