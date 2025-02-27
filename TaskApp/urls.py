from django.urls import path
from . import views

urlpatterns = [

    #------------------------- homepage urls --------------------------#

    path('', views.index, name=""),

    #---------------------- CRUD Operation urls ----------------------#

    path('createTask', views.createTask, name="createTask"),
    path('updateTask/<int:param>/', views.updateTask, name="updateTask"),
    path('deleteTask/<int:param>/', views.deleteTask, name="deleteTask"),


    #---------------------- user registration urls ----------------------#

    path('register', views.register, name="register"),


    #---------------------- user login urls ----------------------#

    path('login', views.login, name="login"),


    #------------------------------ dashboard urls -------------------------#

    path('dashboard', views.dashboard, name="dashboard"),


    #------------------------------ user profile/update urls -------------------------#

    path('updateUser', views.updateUser, name="updateUser"),


    #------------------------------ user profile/update urls -------------------------#

    path('deleteUser', views.deleteUser, name="deleteUser"),


    #---------------------- user logout urls ----------------------#

    path('logout', views.logout, name="logout"),
]
