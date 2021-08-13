from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import TodoList, TodoItem
from django.template import loader
from django.shortcuts import redirect
from .forms import TaskForm
# Create your views here.

def index(request):
    list_todo = TodoList.objects.all()
    items = TodoItem.objects.all()
    template = loader.get_template('polls/index.html')
    context = {
        'todolists': list_todo,
        'todoitems': items
    }
    return HttpResponse(template.render(context, request))

def detail(request, list_id):
    try:
        todolist = TodoList.objects.get(id=list_id)
    except TodoList.DoesNotExist:
        raise Http404("This list does not exist")
    items_list = TodoItem.objects.filter(todo_list=todolist)
    context = {
        'todolist': todolist,
        'items_list': items_list
    }
    return render(request, 'polls/detail.html', context)

def create(request):
    if request.method =='GET':
        return render(request, 'polls/createlist.html')

    name = request.POST['name']
    TodoList.objects.create(list_name = name)
    lists = TodoList.objects.all()
    context = {
        'todolists': lists
    }
    return render(request, 'polls/index.html', context)

def delete_task(request, pk):
    try:
        task = TodoList.objects.get(id=pk)
        task.delete()
    except TodoList.DoesNotExist:
        raise Http404("This list does not exist")
    lists = TodoList.objects.all()
    context = {
        'todolists': lists
    }
    return render(request, 'polls/index.html', context)

def delete_sub_task(request, pk):
    try:
        task = TodoItem.objects.get(id=pk)
        t = task.todo_list.id
        task.delete()
    except TodoItem.DoesNotExist:
        raise Http404("This list does not exist")
    return redirect(f'http://127.0.0.1:8000/polls/{t}/')

def createsub(request, pk):
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f"http://127.0.0.1:8000/polls/{pk}/")
    return render(request, "polls/createsublist.html", {"task_form": form})

def update_task(request, pk):
    if request.method =='GET':
        return render(request, 'polls/update_task.html')
    obj = TodoList.objects.get(id=pk)
    name = request.POST['name']
    obj.list_name = name
    obj.save()
    lists = TodoList.objects.all()
    context = {
        'todolists': lists
    }
    return render(request, 'polls/index.html', context)

def update_sub_task(request, pk):
    task = TodoItem.objects.get(id=pk)
    form = TaskForm(instance=task)
    t = task.todo_list.id
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect(f"http://127.0.0.1:8000/polls/{t}/")
    context = {
        'task_edit_form': form
    }
    return render(request, "polls/update_sub_task.html", context)