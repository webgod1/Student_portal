from django.shortcuts import render, redirect
# from .models import Notes\
from django.views import generic
from .form import *
from .models import *
# Create your views here.
from youtubesearchpython import VideosSearch
import requests

def Home(request):
    return render(request, 'home.html')

def notes(request):
    if request.method == 'POST':
        form = NoteForms(request.POST)
        if form.is_valid():
            user = Notes(user=request.user, title=request.POST['title'], description=request.POST['description'])
            user.save()
    else:
        form = NoteForms()
    user = Notes.objects.filter(user=request.user)
    return render(request, 'note.html', {'note': user, 'form': form})

def delete(request, pk=None):
    Notes.objects.get(id=pk).delete()
    return redirect('/note')

class Notedetails(generic.DetailView):
    model = Notes

def homework(request):
    if request.method == "POST":
        form = HomeWork(request.POST)
        if form.is_valid():
            try:
                is_finished = request.POST['finished']
                if is_finished == 'on':
                    is_finished = True
                else:
                    is_finished = False
            except:
                is_finished = False
                
            homeworks = Homework(
                user=request.user, 
                title=request.POST['title'],
                description=request.POST['description'], 
                due=request.POST['due'], 
                finished=is_finished,
                subject=request.POST['subject'])
            homeworks.save()
    else:
        form = HomeWork()
    homeworks = Homework.objects.filter(user=request.user)
    if len(homeworks) == 0:
        homework_done = True
    else:
        homework_done =False
    
    return render(request, 'homework.html', {'homework': homeworks, 'form': form})

def update_homework(request, pk=None):
    homework = Homework.objects.get(id=pk)
    if homework.finished == True:
        homework.finished = False
    else:
        homework.finished = True
    homework.save()

    return redirect('homework')


def delete_homework(request, pk=None):
    homework = Homework.objects.get(id=pk).delete()
    return redirect('homework')

def youtube(request):
    if request.method == 'POST':
        youtube_ = Youtube(request.POST)
        text = request.POST['text']
        video = VideosSearch(text, limit=15)
        result_list = []
        for i in video.result()['result']:
            result_dic = {
                'input': text,
                'title': i['title'],
                'duration': i['duration'],
                'thumbnail': i['thumbnails'][0]['url'],
                'link': i['link'],
                'channel': i['channel']['name'],
                'views': i['viewCount']['short'],
                'published': i['publishedTime'],
            }
            des = ''
            if i['descriptionSnippet']:
                for j in i['descriptionSnippet']:
                    des += j['text']
            result_dic['description'] = des
            result_list.append(result_dic)
        return render(request, 'youtube.html', {'youtube': youtube_, 'results': result_list})
    else:
        youtube_ = Youtube()
    return render(request, 'youtube.html', {'youtube': youtube_})

def todo(request):
    if request.method == "POST":
        form = Todo_form(request.POST)
        if form.is_valid():
            todo_list = Todo(description=request.POST['description'], user=request.user)
            todo_list.save()
    form = Todo_form()
    todo_list = Todo.objects.filter(user=request.user)
    return render(request, 'todo.html', {'list': todo_list, 'form': form})


def delete_todo(request, pk=None):
    Todo.objects.get(id=pk).delete()
    return redirect('/todos')

def books(request):
    if request.method == 'POST':
        youtube_ = Youtube(request.POST)
        text = request.POST['text']
        url = 'https://www.googleapis.com/books/v1/volumes?q='+text
        r = requests.get(url)
        answer = r.json()
        result_list = []
        for i in range(10):
            result_dic = {
                'title': answer['items'][i]['volumeInfo']['title'],
                'subtitle': answer['items'][i]['volumeInfo'].get('subtitle'),
                'description': answer['items'][i]['volumeInfo'].get('description'),
                'count': answer['items'][i]['volumeInfo'].get('pageCount'),
                'categories': answer['items'][i]['volumeInfo'].get('categories'),
                'rating': answer['items'][i]['volumeInfo'].get('pageRating'),
                'thumbnails': answer['items'][i]['volumeInfo'].get('imageLinks').get('thumbnail'),
                'preview': answer['items'][i]['volumeInfo'].get('previewLink')
                 }
            result_list.append(result_dic)
        return render(request, 'book.html', {'form': youtube_, 'results': result_list})
    else:
        youtube_ = Youtube()
    return render(request, 'book.html', {'form': youtube_})
