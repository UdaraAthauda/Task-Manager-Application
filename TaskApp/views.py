from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.models import User

#--------------------------- user authentication --------------------------#

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import auth

from django.contrib.auth.decorators import login_required


# Create your views here.

#-------------------------- homepage --------------------------#

def index(request):

    return render(request, 'index.html')


#-------------------------- CRUD - create tasks page --------------------------#

@login_required(login_url='login')
def createTask(request):

    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid:
            task = form.save(commit=False)
            task.user = request.user
            task.save()

            return redirect('dashboard')

    form = TaskForm()

    dict = {'form': form}

    return render(request, 'createTask.html', context=dict)


#-------------------------- CRUD - update tasks page --------------------------#

@login_required(login_url='login')
def updateTask(request, param):

    updateDetails = Task.objects.get(id=param)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=updateDetails)

        if form.is_valid:
            form.save()

            return redirect('dashboard')

    form = TaskForm(instance=updateDetails)

    dict = {'form': form}

    return render(request, 'updateTask.html', context=dict)


#-------------------------- CRUD - delete a task --------------------------#

@login_required(login_url='login')
def deleteTask(request, param):
    if param:
        deleteDetail = Task.objects.get(id=param)

        deleteDetail.delete()

        return redirect('dashboard')
    

#-------------------------- user creation / registration --------------------------#

def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('login')

    form = UserRegisterForm()

    dict = {'form': form}

    return render(request, 'register.html', context=dict)


#-------------------------- user login --------------------------#

def login(request):

    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password= password)

            if user is not None:
                auth.login(request, user)

                return redirect('dashboard')
 
    form = UserLoginForm()

    dict = {'form': form}

    return render(request, 'login.html', context=dict)


#---------------------------------- dashboard -----------------------------------------#

@login_required(login_url='login')
def dashboard(request):
    current_user = request.user.id

    tasks = Task.objects.all().filter(user=current_user)

    dict = {'tasks': tasks}

    return render(request, 'dashboard.html', context=dict)


#------------------------------ user profile/update page --------------------------#

@login_required(login_url='login')
def updateUser(request):
    currentUser = request.user

    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=currentUser)

        if form.is_valid():
            form.save()

            return redirect('dashboard')

    form = UserUpdateForm(instance=currentUser)

    dict = {'form': form}

    return render(request, 'updateUser.html', context=dict)


#------------------------------- delete user -----------------------------#

@login_required(login_url='login')
def deleteUser(request):
    if request.method == 'POST':
        deletingUser = User.objects.get(username = request.user)

        deletingUser.delete()

        return redirect('logout')
    
    return render(request, 'deleteUser.html')


#----------------------------------- user logout --------------------------------------#

def logout(request):
    auth.logout(request)

    return redirect('')