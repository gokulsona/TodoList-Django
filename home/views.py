from django.shortcuts import render, HttpResponse
from .models import Task

# Create your views here.
def home(request):
    context={
        'success': False,
        }
    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['desc']
        print(title, desc)
        ins = Task(taskTitle=title, taskDesc=desc)
        ins.save()
    return render(request, 'index.html', context )

def task(request):
    allTasks = Task.objects.all()
    context={
        'task' : allTasks
    }
    return render(request, 'task.html', context)
