from django.test import TestCase
from budget.models import Category, Expense, Project

class ModelTest(TestCase):
    def test_budget_left(self):
        proejct1 = Project.objects.create(
            name = "project1",
            budget = 7000
        )

        category1 = Category.objects.create(
             project  = proejct1,
             name = "software"
        )

        expense = Expense.objects.create(
           project = proejct1,
           amount = 500,
           category =  category1,
           title ='Kahraba'

        )
        self.assertEquals(proejct1.budget_left, 6400)

          