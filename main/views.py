from django.shortcuts import render, redirect
from main.models import TODO

# Create your views here.
def home(request):
    todos = TODO.objects.all()
    return render(request, 'main/home.html', {'todos': todos})

def add_todo(request):
    if request.method == 'GET':
        return render(request, 'main/add.html')
    else:
        title = request.POST['title']
        content = request.POST['content']
        try:
            TODO.objects.create(title=title, content=content, user_id=request.user.id, is_completed=False)
            return redirect('home')
        except Exception as e:
            return redirect('add-todo')

def delete(request, id):
    todo = TODO.objects.get(id=id)
    todo.delete()
    return redirect('home')

def edit(request, id):
    todo = TODO.objects.get(id=id)

    if request.method == 'GET':
        return render(request, 'main/edit.html', context={'todo': todo})
    else:
        todo.title  = request.POST['title']
        todo.content = request.POST['content']

        todo.save()

        return redirect('home')