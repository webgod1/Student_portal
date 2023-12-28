"""student_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home),
    path('note', views.notes),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('detail/<int:pk>', views.Notedetails.as_view(), name='details'),
    path('homework', views.homework, name='homework'),
    path('up/<int:pk>', views.update_homework, name='up'),
    path('del/<int:pk>', views.delete_homework, name='del'),
    path('youtube', views.youtube, name='youtube'),
    path('todos', views.todo, name='todo'),
    path('my_del/<int:pk>', views.delete_todo, name='my_del'),
    path('book/', views.books, name='books')
]
