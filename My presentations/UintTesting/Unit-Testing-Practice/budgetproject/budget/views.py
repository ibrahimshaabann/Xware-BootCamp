from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import Project, Category, Expense
from django.views.generic import CreateView
from django.utils.text import slugify
from .forms import ExpenseForm

def project_list(request):
    project_list = Project.objects.all()
    return render(request, 'project-list.html', {'project_list': project_list})

def project_detail(request, project_slug):
    retrieved_project = get_object_or_404(Project, slug=project_slug)

    if request.method == 'GET':
        category_list = Category.objects.filter(project=retrieved_project)
        return render(request, 'project-detail.html', {'project': retrieved_project, 'expense_list': retrieved_project.expenses.all(), 'category_list': category_list})

    elif request.method == 'POST':
        form = ExpenseForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data['title']
            amount = form.cleaned_data['amount']
            category_name = form.cleaned_data['category']

            category = get_object_or_404(Category, project=retrieved_project, name=category_name)

            Expense.objects.create(
                project=retrieved_project,
                title=title,
                amount=amount,
                category=category
            )

    return render(request, 'project-list.html', {'success':'Yes'})


class ProjectCreateView(CreateView):
    model = Project
    template_name = 'add-project.html'
    fields = ('name', 'budget')

    def form_valid(self, form):
        self.object = form.save()

        categories = self.request.POST.get('categoriesString').split(',')
        for category in categories:
            Category.objects.create(
                project=Project.objects.get(id=self.object.id),
                name=category
            )

        return redirect(self.object)
