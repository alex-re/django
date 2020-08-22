from django.shortcuts import render
from django.http import HttpResponse  # if we have external html files we can comment this importing.

from .models import Post  # "." means models in this directory.

# Create your views here.


# posts = [
#     {
#         'author':'khodam',
#         'title':'Blog post 1',
#         'content':'First post content',
#         'date_posted':'Agust 27, 2018'
#     },
#     {
#         'author':'chalghoos',
#         'title':'Blog post 2',
#         'content':'Second post content',
#         'date_posted':'Agust 30, 2020'
#     }
# ]


def home(request):
    context = {
        # 'posts':posts
        'posts':Post.objects.all()
    }

    # return HttpResponse("<h1> Blog Home </h1>")
    return render(request, 'blog/home.html', context)  # ~/django/django_project/blog/templates/blog/home.html


def about(request):
    # return HttpResponse("<h1> Blog About </h1>")
    return render(request, 'blog/about.html', {'title':'About'})

