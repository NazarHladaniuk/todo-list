from django.shortcuts import render
from django.views import generic

from todo.models import Tag, Task


def index(request):
    tasks = Task.objects.all()
    context = {
        "tasks": tasks,
    }
    return render(request, "todo/index.html", context=context)


class CarListView(generic.ListView):
    model = Tag
