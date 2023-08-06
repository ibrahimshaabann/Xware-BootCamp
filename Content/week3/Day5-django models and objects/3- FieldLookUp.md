# Retrieve books filtered by a condition
java_books = Book.objects.filter(title="Java")
python_books = Book.objects.filter(title="Python", author=author)
<<Field Lookup:>>
java_books = Book.objects.filter(title__contains="Java")
# Filter books with titles containing "Python" and published after 2020
python_books = Book.objects.filter(title__contains="Python", published__year__gt=2020)
# Exclude books with titles containing "Java"
non_java_books = Book.objects.exclude(title__contains="Java")
# Get a single book by its title
book = Book.objects.get(title="Sample Book")
# Limit the number of retrieved books
limited_books = Book.objects.all()[:5]
<<Order By, Sort, Group By, Count:>>
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    class Meta:
        ordering = ['-title']  # To order books by title in descending order
# Order books by title in ascending order
sorted_books = Book.objects.order_by('title')
# Count the number of books published after 2020
count_books_after_2020 = Book.objects.filter(published__year__gt=2020).count()
# Group books by the author's name
from django.db.models import Count
books_by_author_count = Book.objects.values('author__name').annotate(count=Count('id'))
