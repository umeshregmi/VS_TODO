from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'main/home.html')

def add_todo(request):
    return render(request, 'add.html')