from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

# Create your views here.

def index(request):
    tasks = Task.objects.all()
    form = TaskForm()

    #vérifier la méthode HTTP
    if request.method == "POST":
        #instancier le formulaire avec les données 
        form = TaskForm(request.POST)
        #tester la validité du formulaire
        if form.is_valid():
            #enregister les données
            form.save()
            #rediriger vers l'URL "index"
            return redirect("index")

    return render(request,"index.html",{"tasks" : tasks, "task_form" : form})


def update(request,pk):

    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()

            return redirect("index")
    
    return render(request, "update.html",{"edit_task_form":form})



def delete(request,pk):

    task = Task.objects.get(id=pk)

    if request.method == "POST" :
        task.delete()
        return redirect("index")
    
    return render(request,"delete.html",{"task" : task})


