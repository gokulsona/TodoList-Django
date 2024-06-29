from django.shortcuts import render, HttpResponse, redirect
from .models import Task, Completed


def task(request):   
    task = Task.objects.filter(iscompleted=False)
    completed = Task.objects.filter(iscompleted=True)
    context={
        'task' : task,
        'completed':completed
    }
    return render(request, 'task.html', context)

def home(request):
    context={
        'success': False,
        }
    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['desc']  
        ins = Task(taskTitle=title, taskDesc=desc)
        ins.save()
    return render(request, 'index.html', context )


#delete
def delete(request, id):
    task = Task.objects.get(id=id)    
    if request.method=="POST":
        task.delete()
        return redirect('task')
    
#completed
def completed(request, id):
    task = Task.objects.get(id=id)
    task.iscompleted=True        
    task.save()
    return redirect('task1')


def task1(request):   
    task = Task.objects.filter(iscompleted=False)
    completed = Task.objects.filter(iscompleted=True)
    context={
        'task' : task,
        'completed':completed
    }
    return render(request, 'task.html', context)
        
def edit(request, id):
    # updating
    task = Task.objects.get(id=id)  
    context ={
        'title':task.taskTitle,
        'description':task.taskDesc,
        'id':id
    }
    return render(request, 'edit.html', context)

def update(request, id):
    task = Task(id=id)
    task.taskTitle = request.POST['title']
    task.taskDesc = request.POST['desc']  
    import datetime
    updated_at = datetime.datetime.now()
    task.time = updated_at
    task.save()
    return redirect('task')    