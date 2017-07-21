from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Todo


def index(request):
    context_dict = {}

    todo_list = Todo.objects.all()
    context_dict["todos"] = todo_list

    return render(request, 'todo/index.html', context=context_dict)


def detail(request, slug):
    context_dict = {}

    todo_list = Todo.objects.get(slug)
    context_dict["title"] = todo_list["title"]
    #context_dict["body"] = todo_list["body"]

    todo_item = Todo.objects.get(title=todo.slug)

    return render(request, 'todo/detail.html', context=context_dict)


def about(request):
    return HttpResponse("This is todo app!")
