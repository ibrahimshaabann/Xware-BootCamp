# ***CRUD Operations***

## ***1. Create***

>> ### Create an author

```python
author = Author(name="John Doe")
author.save()
```

>> ### Create a book associated with the author

```python
book = Book(title="Sample Book", author=author)
book.save() # Sav4 the object to database
```

>> ### Create a reader using the 'create' method

```python
reader = Reader.objects.create(name="Eman", author=author)
```

## ***2. Read***

>> ### Retrieve all books
```python
books = Book.objects.all()
```

>> ### Retrieve a book by its ID
```python
book = Book.objects.get(id=1)
```

>> ### Retrieve books by a specific author's name
```python
books_by_author = Book.objects.filter(author__name="John Doe")
```

## ***3. Update***

>> ### Update a book's title
```python
book.title = "New Title"
book.save()
```

## ***4. Delete***

>> ### Delete a book
```python
book = Book.objects.get(id=1)
book.delete()
```


