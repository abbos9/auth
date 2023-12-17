from django.shortcuts import render, redirect

from user.forms import UserModelForm
from user.models import User


def login(request):
    data = request.POST
    if request.POST:
        username = data.get('username')
        password = data.get('password')
        print(username, password)
        a = User.objects.filter(username=username, password=password).first()
        print(a)
        if a:
            return redirect('users')

    return render(request, 'login.html')


def reg(request):
    if request.POST:
        data = UserModelForm(request.POST, files=request.FILES)
        if data.is_valid():
            data.save()
        return redirect('login')
    return render(request, 'signup.html')


def users(request):
    data = User.objects.all()
    return render(request, 'users.html', {"users": data})


def user(request):
    return render(request, 'user.html')


