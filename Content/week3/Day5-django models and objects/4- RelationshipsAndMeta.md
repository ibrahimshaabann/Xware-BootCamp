
## *Relationships and Meta*

**ORM allows you to define relationships between models, such as one-to-many (ForeignKey) and many-to-many (ManyToManyField) relationships. In our example, the `Book` model has a `ForeignKey` relationship with the `Author` model, and the `Reader` model has a `ManyToManyField` relationship with the `Book` model.**

```python
# Access the related author object
book = Book.objects.get(id=1)
author = book.author
```

The database query is not executed until the data is accessed:
```python
books_queryset = Book.objects.filter(title__contains="Python")

# The database query is executed when data is accessed
for book in books_queryset:
    print(book.title)
```

### One-to-One Relationship:

```python
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
```

### Many-to-Many Relationship:

```python
reader = Reader.objects.create(name="Alice")
book1 = Book.objects.create(title="Python Basics", published_year=2023, author=author)
book2 = Book.objects.create(title="Django Web Development", published_year=2022, author=author)

reader.borrowed_books.add(book1, book2)
borrowed_books = reader.borrowed_books.all()
```

### One-to-Many Relationship:

```python
Author.objects.filter(id=1).first().book_set.all()
```

Custom managers:

```python
available_books = Book.available_objects.all()
```

Please note that this Markdown representation is intended to display the information, and you should implement and adapt it to your Django project with appropriate models and usage.
