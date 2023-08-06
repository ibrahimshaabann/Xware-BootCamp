>> ## In our example, we'll create a library project with three tables: Book, Author, and Reader, and use ORM to interact with the database

<Create models.py>

### Importing libraries
```python
from django.db import models
from django.db.models.query import QuerySet
```

### Creating author class
```python
class Author(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
```

### Creating Author class
>> ### There is a one to many relationship between Author and books
```sql
class Book(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    published_year = models.IntegerField()
    published = models.DateField(null=True)
    available = models.BooleanField(default=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE) 
    
    class Meta:
    '''
        This class identifies data (description) about data
    '''
        ordering = ['name'] #order by name in ascending order, ['-name'] means descending order
```

### This is BookDetail class
>> ### It's a one to one relationship  between Book class and BookDEtail class
```python
class BookDetail(models.Model):
    language = models.CharField(max_length=100)
    page_count = models.IntegerField()
    book = models.OneToOneField(Book, on_delete=models.CASCADE)
```

### This is Reader Class
>> ### There is a M:N relationship between Reader and books
```python
class Reader(models.Model):
    name = models.CharField(max_length=100)
    borrowed_books = models.ManyToManyField(Book)
```



### Overriding
>> ### Manager class is an interface that provides some functions between is responsible for sending objects to database and getting objects from databaseand turn it to python objects

```python
class AvailableBookManager(models.Manager): 
    
# Any list you will your return from database will be returned only if its available attribute = true in book class Overriding function get_queryset in Manager class
    def get_queryset(self) -> QuerySet:
        return super().get_queryset()  # Query set is the returned list of objecs
```

## After any modification in models you have to Write these lines

```bash
python manage.py makemigrations
python manage.py migrate
```
