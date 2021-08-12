from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import TodoList, TodoItem
from django.template import loader
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