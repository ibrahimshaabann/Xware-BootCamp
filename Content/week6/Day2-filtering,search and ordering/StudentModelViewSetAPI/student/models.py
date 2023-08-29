from django.db import models
from Books.models import Book

class Student(models.Model):
    name = models.CharField(max_length=70)
    age = models.IntegerField()
    dep = models.CharField(verbose_name="department", max_length=2, blank=True)
    borrowed_book =models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)


    class Meta :
        db_table = "Student Table"
        get_latest_by = ["-age", "name"] # descending age first, ascending name
        

    def __str__(self) -> str:
        return f"\nName {self.name} \nAge: {self.age} \nDepartment:{self.dep}\n"
    

