from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.db.models import Q

from .models import Task, Category
from .forms import TaskForm, CategoryForm

# Create your views here.

# register view


def home(request):
    return render(request, 'task/home.html')


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # log in the user immediately
            login(request, user)
            # redirect the user to the task_list
            return redirect('task_list')
    else:
        form = UserCreationForm()
    return render(request, 'task/register.html', {'form': form})

# CRUD operations


@login_required
# list all the task and categories for a particular user
def task_list(request):
    # print(request.user.is_authenticated)
    # if request.user.is_authenticated == False:
    #     print("hello world")
    #     return redirect('login')

    category_id = request.GET.get('category')
    search_query = request.GET.get('search', )
    status_filter = request.GET.get('status')
    priority_filter = request.GET.get('priority')
    # tasks that belongs to the logged in user
    tasks = Task.objects.filter(user=request.user)

    # Apply category filter
    if category_id:
        tasks = tasks.filter(category_id=category_id)

    # Apply search filter on title and description
    if search_query:
        tasks = tasks.filter(
            Q(title__icontains=search_query) | Q(
                description__icontains=search_query)
        )

    # Apply status filter if selected
    if status_filter:
        tasks = tasks.filter(status=status_filter)

    # Apply priority filter if selected
    if priority_filter:
        tasks = tasks.filter(priority=priority_filter)

    # Retrieve all categories for the filter dropdown
    categories = Category.objects.filter(user=request.user)
    return render(request, 'task/task_list.html', {
        'tasks': tasks,
        'categories': categories,
        'search_query': search_query,
        'status_filter': status_filter,
        'priority_filter': priority_filter
    })


@login_required
# create new task
def task_create(request):
    # if the the http request method is Post then save it to the task obj
    if request.method == "POST":
        form = TaskForm(request.POST, user=request.user)
        if form.is_valid():
            task = form.save(commit=False)
            # owner of the task is the current logged in user
            task.user = request.user
            task.save()
            return redirect('task_list')
        # else allow for the creation of a new form
    else:
        form = TaskForm(user=request.user)
    return render(request, 'task/task_form.html', {'form': form})


@login_required
# get a task by its id and update it
def task_update(request, pk):
    # getting the task by its pk and current user
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == "POST":
        # the instance passed to the fields will be the current task
        form = TaskForm(request.POST, instance=task, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('task_list')

    else:
        form = TaskForm(instance=task, user=request.user)
    return render(request, 'task/task_form.html', {'form': form})


@login_required
# get the task by its ID and delete it
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == "POST":
        task.delete()
        return redirect('task_list')
    return render(request, 'task/task_confirm_delete.html', {'task': task})


@login_required
def category_list(request):
    categories = Category.objects.filter(user=request.user)
    return render(request, 'task/category_list.html', {'categories': categories})


@login_required
def category_create(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'task/category_form.html', {'form': form})


@login_required
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk, user=request.user)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'task/category_confirm_delete.html', {'category': category})
