<<Relationships and Meta >>
{{ORM allows you to define relationships between models, such as one-to-many (ForeignKey) and many-to-many (ManyToManyField) relationships.}}
{{In our example, the Book model has a ForeignKey relationship with the Author model, and the Reader model has a ManyToManyField relationship with the Book model.}}
<<Forien Key Objects>>
book = Book.objects.get(id=1)
author = book.author  # Access the related author object
<<QuerySets Are Lazy:>>
books_queryset = Book.objects.filter(title__contains="Python")
# The database query is not executed until the data is accessed
for book in books_queryset:
    print(book.title)
    
    
    
1-One-to-One Relationship:
from django.db import models
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
Many-to-Many
reader = Reader.objects.create(name="Alice")
book1 = Book.objects.create(title="Python Basics", published_year=2023, author=author)
book2 = Book.objects.create(title="Django Web Development", published_year=2022, author=author)
reader.borrowed_books.add(book1, book2)
borrowed_books = reader.borrowed_books.all()
3-One-to-Many Relationship:
Author.objects.filter(id=1).first().book_set.all()
custom managers
available_books = Book.available_objects.all()
