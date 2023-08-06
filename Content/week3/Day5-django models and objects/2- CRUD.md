--------------------------- CRUD --------------------------------
<<Create Objects and Save Changes>>:
author = Author(name="John Doe")
author.save()
book = Book(title="Sample Book", author=author)
book.save()
reader = Reader.objects.create(name="Eman", author=author)
<<Retrieve Objects:>>
# Retrieve all books
books = Book.objects.all()
<<Retrieve One Object:>>
book = Book.objects.get(id=1)
<<Update Object:>>
book = Book.objects.get(id=1)
book.title = "New Title"
book.save()
<<Delete Object>>
book = Book.objects.get(id=1)
book.delete()
books_by_author = Book.objects.filter(author__name="John Doe")
_________________________________________________________________________________________
