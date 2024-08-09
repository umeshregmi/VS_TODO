from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        uname = request.POST['username']
        email = request.POST['email']
        pswd = request.POST['password']

        try:
            user = User.objects.create_user(username=uname, password=pswd, first_name=fn, last_name=ln, email=email)

            print('***********')
            print(user)

            if user is not None:
                return redirect('signin')
            else:   
                return redirect('register')
    
        except Exception as e:
            print(e)
            print('i am except *******')
            return redirect('register')

def signin(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        uname = request.POST['username']
        pswd = request.POST['password']

        user = authenticate(username=uname, password=pswd)
        if user is not None:
            login(request, user)

            return redirect('home')
        else:
            return redirect('signin')

def signout(request):
    logout(request)
    return redirect('signin')