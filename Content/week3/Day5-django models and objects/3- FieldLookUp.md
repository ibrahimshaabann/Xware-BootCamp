# *Filed Lookup*

***1. Retrieve books filtered by `title`***

```python
java_books = Book.objects.filter(title="Java")
python_books = Book.objects.filter(title="Python", author=author)
```
<br>

***2. Filter books with titles containing `"Java"`***

```python
java_books = Book.objects.filter(title__contains="Java")
```

<br>

***3. Filter books with titles containing `"Python"` and published after 2020***

```python
python_books = Book.objects.filter(title__contains="Python", published__year__gt=2020)
```

<br> 

***4. Exclude books with titles containing `"Java"`***

```python
non_java_books = Book.objects.exclude(title__contains="Java")
```

<br>

***5. Get a single book by its `title`***

```python
book = Book.objects.get(title="Sample Book")
```

<br>

***6. Limit the `number` of retrieved books***

```python
limited_books = Book.objects.all()[:5]
```

<br>

***7. Order books by `title` in ascending order***

```python3
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['title']  # To order books by title in ascending order
```

<br>

***8. Count the number of `books` published after 2020***

```python
count_books_after_2020 = Book.objects.filter(published__year__gt=2020).count()
```

<br>

***9. Group books by the `author's name`***

```python
from django.db.models import Count
books_by_author_count = Book.objects.values('author__name').annotate(count=Count('id'))
```

